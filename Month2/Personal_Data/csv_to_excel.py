import pandas as pd

def csv_to_xlsx(csv_path='data.csv',excel_path='data.xlsx'):
    df = pd.read_csv(csv_path, dtype={'phone_no':str})
    df.to_excel(excel_path, index = False)
    print(f"Saved {excel_path}")

if __name__ == '__main__':
    csv_to_xlsx('data.csv','data.xlsx')
