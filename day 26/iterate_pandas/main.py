student_dict={
    "student":["sam","ram","hari"],
    "score":[20,30,40]
}
#looping through dictionaries
for (key,value) in student_dict.items():
    print(value)
    

#iterating through pandas

import pandas as pd

student_data_frame=pd.pandas.DataFrame
(student_dict)
print(student_data_frame)


#loop trough rows of dataframe
for (index, row) in student_data_frame.iterrows():
    print(row.student)