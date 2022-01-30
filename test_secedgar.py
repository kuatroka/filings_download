from datetime import date
# from secedgar import filings
from secedgar import filings, ComboFilings, DailyFilings, CompanyFilings, QuarterlyFilings
from secedgar.client import NetworkClient


############## doesn't work - constantly brings the same filing across the range of dates
# def test_download():
# a = NetworkClient(rate_limit=1,user_agent="Mozilla")

# limit_to_form13 = lambda f: f.form_type in ("13F-HR", "13F-HR/A") 
# # limit_to_form13 = lambda f: f.form_type == "13F-HR/A"

# daily_filings_limited = filings(start_date=date(1993, 1 ,1),
#                                 end_date=date(2021, 3, 31),
#                                 client=a,
#                                 # filing_type=FilingType.FILING_10Q)
#                                 entry_filter=limit_to_form13)
# daily_filings_limited.save("./data_13F")

############### Daily Filings -  - works well, but downloads only filings from one day

# a = NetworkClient(rate_limit=1,user_agent="Mozilla")
# # limit_to_form13 = lambda f: f.form_type in ("13F-HR", "13F-HR/A") 
# limit_to_form13 = lambda f: f.form_type == "13F-HR"

# daily_filings_limited = DailyFilings(date=date(2020, 1 ,15),
#                                                    client=a,
#                                 entry_filter=limit_to_form13)

# daily_filings_limited.save("./data_13F")
################

############### Quarterly Filings - works well, but downloads only filings from one quarter 

# a = NetworkClient(rate_limit=5,user_agent="Mozilla")
# limit_to_form13 = lambda f: f.form_type in ("13F-HR", "13F-HR/A") 
# # limit_to_form13 = lambda f: f.form_type == "13F-HR"
# for i in range(1, 5):
#     quarterly = QuarterlyFilings(year=2020,
#                                     quarter=i,
#                                     entry_filter=limit_to_form13,
#                                     #  user_agent="Name (email)")
#                                     client=a)

#     quarterly.save("./data_13F")

################

################ Combo Filings - for range of dates
#########  does not work !
# a = NetworkClient(rate_limit=1,user_agent="Chrome")
# # limit_to_form13 = lambda f: f.form_type in ("13F-HR", "13F-HR/A") 
# limit_to_form13 = lambda f: f.form_type == "13F-HR"

# combo_filings = ComboFilings(start_date=date(1993, 1, 1),
#                              end_date=date(2014, 12, 31),
#                              client=a,
#                              entry_filter=limit_to_form13)


# combo_filings.save("./data_13F")

###################### My version for downloading across range of years

a = NetworkClient(rate_limit=4,user_agent="Mozilla")
limit_to_form13 = lambda f: f.form_type in ("13F-HR", "13F-HR/A") 
# limit_to_form13 = lambda f: f.form_type == "13F-HR"
def filings_range_years_download(list_of_years):
    # years = [list_of_years]
    for i in list_of_years: 
        
        for j in range(1, 5):
            quarterly = QuarterlyFilings(year=i,
                                        quarter=j,
                                        entry_filter=limit_to_form13,
                                        client=a)
            print(f"Year {i} Quarter {j}")
            quarterly.save("./data_13F")


def main():
    filings_range_years_download([2021])


if __name__ == "__main__":
    main()


