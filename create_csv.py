import pandas as pd

logf = open("error.log", "w")
try:
    print("running.....")
    main_table = pd.read_csv("filea1.csv", usecols=['title', 'jan', 'feb'])
    child_table = pd.read_csv("fileb.csv", usecols=['title', 'mar', 'apr'])
    table_after_join = main_table.merge(child_table, on='title')
    table_after_join.to_csv("output.csv", index=False)
except Exception as e:
    print("An error occur while processing \n")
    logf.write("Failed to process {0}\n".format(str(e)))