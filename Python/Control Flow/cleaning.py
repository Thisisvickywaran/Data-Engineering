
files=['report,csv','DATA.csv','Final.Txt']

for file in files:
    file=file.strip().lower().replace('.txt','.csv')
    print(f"Processing {file}")