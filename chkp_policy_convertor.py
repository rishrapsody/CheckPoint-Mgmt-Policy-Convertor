import pandas as pd

#function to list of  multiple objects count per column
def get_diff(df):
    tdict = {}
    for column in df:
        if column.lower() in excluded_list:
            continue
        else:
            tlist = []
            clist = []
            #loop to detect cells with ';' or '\n' char in each coulumn
            for i,j in df[column].iteritems():
                if type(j) == str:
                    if ';' in j or '\n' in j:
                        tlist.append(j)
            #loop to create temporary list of such cells per column with object count
            for i in tlist:
                #x = i.split('\n')
                #clist.append(len(x))
                if '\n' in i:
                    x = i.split('\n')
                    clist.append(len(x))
                elif ';' in i:
                    x = i.split(';')
                    clist.append(len(x))
            #creating dict for each column name with the respective max object count(This is to insert additional columns
            if len(clist) > 0:
                tdict[column] = max(clist)
            else:
                tdict[column] = 1
    return(tdict)

#function to insert new columns based on max object count per column
def add_new_columns(df,tdict):
    for k,v in tdict.items():
        if k.lower() in excluded_list:
            continue
        else:
            #code to insert new columns based on data from tdict dictionary
            if v > 1:
                insert_at = df.columns.get_loc(k)
                for i in range(v):
                    if i+2 <= v:
                        header_name = "{}.{}".format(k,i+2)
                        df.insert(insert_at+1,header_name,"")
                        insert_at = insert_at + 1
    return(df)

#function to split existing cells with multiple objects(separated by \n or ;)
def split_columns(df_1,tdict):
    for k,v in tdict.items():
        if k.lower() in excluded_list:
            continue
        else:
            #code to split cells with multiple objects and expand into newly added columns per row
            if v > 1:
                for i, j in df_1[k].iteritems():
                    if type(j) == str:
                        if ';' in j or '\n' in j:
                            if '\n' in j:
                                new = df_1[k].str.split('\n',expand=True)
                            elif ';' in j:
                                new = df_1[k].str.split(';', expand=True)
                            try:
                                for i in range(v):
                                    if i+2 <= v:
                                        col = "{}.{}".format(k,i+2)
                                        df_1[col] = new[i+1]
                            except KeyError:
                                pass


#function to remove unwanted space and special chars for each cell after split
def remove_unwanted(df):
    for column in df:
        if column.lower() in excluded_list:
            continue
        else:
            #code to remove unwanted space and semicolon at the end of object name
            for i,j in df[column].iteritems():
                if type(j) == str:
                    if '"' in j or '\n' in j:
                        df.at[i, column] = str(df.at[i, column]).split('\n')[0].strip('"').replace(';','').replace('"', '')
                    else:
                        df.at[i, column] = str(df.at[i, column]).strip().split(';')[0].replace(';', '').replace('"', '')


#functin to fix header name for columns with multiple objects
def fix_headers(df1,tdict):
    for k,v in tdict.items():
        if k.lower() in excluded_list:
            continue
        else:
            #code to fix header name of the columns where object count is more than 1
            if v > 1:
                first_header = "{}.{}".format(k, 1)
                df1.rename(columns={k: first_header},inplace=True)
    df1.to_csv("converted.csv",index=False)


# code execution starts from here
if __name__ == "__main__":
    excluded_list = ['position','comments','log','action','logging','protocol']  #list of columns to exclude in checks
    df = pd.read_csv("input/Book7.csv")     #load csv using pandas
    tdict = get_diff(df)                    #func to get multiple object count per column
    df_1 = add_new_columns(df,tdict)        #func to insert new columns
    split_columns(df_1,tdict)               #func to split existing cells with multiple objects
    remove_unwanted(df)                     #func to remove extra space and special chars
    df['comments'].fillna("NA",inplace=True)    #fill blanks in comments column with NA
    df1 = df.ffill(axis='columns',limit=30)     #fill empty cell with value from value in previous column
    fix_headers(df1,tdict)                      #func to fix header name

