"""Module for calculating the period and the price per kWh given a specific date in spanish TD tariffs."""

from abc import abstractmethod
from datetime import datetime

import holidays

from .const import (
    HOLY_FRIDAYS,
    HOUR_8,
    HOUR_10,
    HOUR_14,
    HOUR_18,
    HOUR_22,
    P1,
    P2,
    P3,
    P4,
    P5,
    P6,
    PERIODS_30TD,
    SATURDAY,
    SUNDAY,
)


class TariffTD:
    """Tariff TD base class."""

    def __init__(self: "TariffTD") -> None:
        """Initialize spanish holidays."""
        self._holidays = holidays.country_holidays("ES")
        # Remove "Viernes Santo"
        for v in HOLY_FRIDAYS:
            self._holidays.pop(v)

    @abstractmethod
    def get_period(self: "TariffTD", date: datetime) -> str:
        """Return the period of specific date."""

    @abstractmethod
    def get_price(self: "TariffTD", date: datetime) -> float:
        """Return the electricity price of specific date."""

    def get_day_prices(self, date: datetime) -> list[float]:
        """Return the electricity prices for each hour of the specified date."""
        return [self.get_price(date.replace(hour=h)) for h in range(24)]


class Tariff20TD(TariffTD):
    """Tariff 2.0 TD definition."""

    _prices = dict[str, float]()

    def __init__(self: "Tariff20TD", p1: float, p2: float, p3: float) -> None:
        """Constructor with receive the price by kWh for each period."""
        super().__init__()
        self._prices = {
            P1: p1,
            P2: p2,
            P3: p3,
        }

    def get_period(self: "Tariff20TD", date=datetime.now()) -> str:
        """Return the period of specific date."""
        hour = date.hour
        if date in self._holidays:
            return P3
        if SATURDAY <= date.weekday() <= SUNDAY:
            return P3
        if hour < HOUR_8:
            return P3
        if hour < HOUR_10:
            return P2
        if hour < HOUR_14:
            return P1
        if hour < HOUR_18:
            return P2
        if hour < HOUR_22:
            return P1
        return P2

    def get_price(self: "Tariff20TD", date=datetime.now()) -> float:
        """Return the electricity price of specific date."""
        period = self.get_period(date)
        return self._prices[period]


class Tariff30TD(TariffTD):
    """Tariff 3.0 TD class definition."""

    def __init__(self: "Tariff30TD", p1: float, p2: float, p3: float, p4: float, p5: float, p6: float):
        """Constructor with receive the price by kWh for each period."""
        super().__init__()
        self._prices = {
            P1: p1,
            P2: p2,
            P3: p3,
            P4: p4,
            P5: p5,
            P6: p6,
        }

    def get_period(self: "Tariff30TD", date=datetime.now()) -> str:
        """Return the period of specific date."""
        hour = date.hour
        if date in self._holidays:
            return P6
        if SATURDAY <= date.weekday() <= SUNDAY:
            return P6

        if hour < HOUR_8:
            return P6

        periods = PERIODS_30TD[date.month - 1]

        if hour < HOUR_10:
            return periods[0]
        if hour < HOUR_14:
            return periods[1]
        if hour < HOUR_18:
            return periods[0]
        if hour < HOUR_22:
            return periods[1]

        return periods[0]

    def get_price(self: "Tariff30TD", date=datetime.now()) -> float:
        """Return the electricity price of specific date."""
        period = self.get_period(date)
        return self._prices[period]
