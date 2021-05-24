####################################################################################
#                                    WARNING                                       #
#                                                                                  #
#                           ONLY RUN WHEN DATABASE IS EMPTY                        #
#                                                                                  #
#                         ELSE MULTIPLE ENRTRIES WILL BE MADE                      #
####################################################################################
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mutual_funds_api.settings')
import django
django.setup()
from basic_app.models import MutualFundsCode, MutualFundsScheme
from mftool import Mftool

def insert_codes_in_db():
    mf = Mftool()
    all_scheme_codes = mf.get_scheme_codes()
    for key, value in all_scheme_codes.items():
        MutualFundsCode.objects.create(code=key, description=value)
    print('done1')

def insert_schemes_in_db():
    mf = Mftool()
    code_objects = MutualFundsCode.objects.all()
    obj_num = 1
    for code_obj in code_objects:
        print(obj_num)
        obj_num += 1
        argu_list = []
        try:
            mf_detail = mf.get_scheme_details(code_obj.code)
            for key, value in mf_detail.items():
                argu_list.append(value)
            scheme_start_date = argu_list[5]['date']
            date_split = scheme_start_date.split('-')
            scheme_start_date = date_split[2]+'-'+date_split[1]+'-'+date_split[0]
            MutualFundsScheme.objects.create(fund_house=argu_list[0],scheme_type=argu_list[1],scheme_category=argu_list[2],
                scheme_code=code_obj,scheme_name=argu_list[4],scheme_start_date=scheme_start_date)
        except Exception:
            continue
    print('done2')

if __name__ == '__main__':
    insert_codes_in_db()
    insert_schemes_in_db()
