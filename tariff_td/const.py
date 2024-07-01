"""Constant definition for Tariff TD."""

P1 = "P1"
P2 = "P2"
P3 = "P3"
P4 = "P4"
P5 = "P5"
P6 = "P6"

PERIODS_30TD = [
    [P2, P1],  # Enero
    [P2, P1],  # Febrero
    [P3, P2],  # Marzo
    [P5, P4],  # Abril
    [P5, P4],  # Mayo
    [P4, P3],  # Junio
    [P2, P1],  # Julio
    [P4, P3],  # Agosto
    [P4, P3],  # Septiembre
    [P5, P4],  # Octubre
    [P3, P2],  # Noviembre
    [P2, P1],  # Diciembre
]

SATURDAY = 5
SUNDAY = 6

HOUR_8 = 8
HOUR_10 = 10
HOUR_14 = 14
HOUR_18 = 18
HOUR_22 = 22

HOLY_FRIDAYS = [
    "2024-03-29",
    "2025-04-18",
    "2026-04-03",
    "2027-03-26",
    "2028-04-14",
    "2029-03-30",
    "2030-04-19",
]
