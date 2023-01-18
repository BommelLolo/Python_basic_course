from dataclasses import dataclass


@dataclass
class Date:
    year: int
    month: int
    day: int

    # second solution
    def __gt__(self, other):
        assert isinstance(other, Date)
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    # first solution
    # def __gt__(self, other):
    #     assert isinstance(other, Date)
    #     res = False
    #     if self.year > other.year:
    #         res = True
    #     elif self.year == other.year:
    #         if self.month > other.month:
    #             res = True
    #         elif self.month == other.month:
    #             if self.day > other.day:
    #                 res = True
    #     return res


@dataclass
class DateRange:
    date_begin: Date
    date_end: Date

    def __gt__(self, other):
        assert isinstance(other, DateRange)
        return self.date_begin > other.date_begin


# second solution
def get_ranges_wo_insurance(insurance_periods: list[DateRange]) -> list[DateRange]:
    res_list = []
    # Sort fo   r list of all insurance's periods for begin date from earlier to later
    insurance_periods.sort()

    # check periods w/o insurance
    for k in range(len(insurance_periods)-1):
        if insurance_periods[k].date_end < insurance_periods[k+1].date_begin:
            period = DateRange(insurance_periods[k].date_end, insurance_periods[k+1].date_begin)
            res_list.append(period)
    return res_list


# first solution
# def get_ranges_wo_insurance(insurance_periods: list[DateRange]) -> list[DateRange]:
#     res_list = []
#     # check length of periods. If less two, than we can't define periods w/o insurance
#     if len(insurance_periods) > 1:
#
#         # Selection Sort for list of all insurance's periods for begin date from earlier to later
#         for i, _ in enumerate(insurance_periods):
#             min_date = i
#             for j in range(i+1, len(insurance_periods)):
#                 if insurance_periods[j].date_begin < insurance_periods[min_date].date_begin:
#                     min_date = j
#
#             insurance_periods[min_date], insurance_periods[i] = \
#                 insurance_periods[i], insurance_periods[min_date]
#
#         # check periods w/o insurance
#         for k in range(len(insurance_periods)-1):
#             if insurance_periods[k].date_end < insurance_periods[k+1].date_begin:
#                 period = DateRange(insurance_periods[k].date_end, insurance_periods[k+1].date_begin)
#                 res_list.append(period)
#
#     else:
#         res_list = []
#     return res_list


if __name__ == '__main__':
    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 6, 25)),
        DateRange(Date(2020, 7, 1), Date(2020, 8, 31)),
        DateRange(Date(2020, 6, 29), Date(2020, 7, 31)),
        DateRange(Date(2020, 10, 1), Date(2020, 12, 31)),
    ]
    get_ranges_wo_insurance(_insurances)

    assert get_ranges_wo_insurance(_insurances) == [
        DateRange(Date(2020, 6, 25), Date(2020, 6, 29)),
        DateRange(Date(2020, 8, 31), Date(2020, 10, 1)),
    ]

    assert get_ranges_wo_insurance([]) == []

    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 7, 15)),
        DateRange(Date(2020, 7, 1), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == []

    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 7, 15)),
        DateRange(Date(2020, 2, 2), Date(2020, 10, 11)),
        DateRange(Date(2020, 7, 16), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == []

    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 7, 15)),
        DateRange(Date(2020, 7, 16), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == [DateRange(Date(2020, 7, 15), Date(2020, 7, 16))]
