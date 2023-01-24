import numpy as np, tabula, pandas as pd, operator as op, sys, re, uuid
from flask import jsonify


def tables(df,df_list):
	num_row = 0; pdf_data = []; pdf_data.append(list(df[num_row])); pdf_columns = list(df[num_row])
	for ls in range(len(df_list)-num_row): page_data = df[ls+num_row].values.tolist(); pdf_data = pdf_data + page_data
	data_pdf = pd.DataFrame(pdf_data); data_pdf = data_pdf.replace(np.nan,''); repete = data_pdf.shape[1]-len(pdf_columns)
	for _ in range(repete): pdf_columns.append('columns')
	return data_pdf

def unknown_columns(tab_cols,col_list):
	table_columns = []
	for elem in range(len(tab_cols)):
		if tab_cols[elem] in col_list: col_name = tab_cols[elem]; table_columns.append(col_name)
		else: table_columns.append('Unknown_column')
	return table_columns

def string_float(string):
    if type(string)==float:
        stf=string
    elif string == '':
        stf=0.0    
    else:
        try:
            a=re.sub(',|Dr|Cr|DR|CR|\W', '', string)
            stf=float(a)
            stf=stf/100
        except:
            stf=string
    return stf   

    

def bank_statement_read(file_path, bank_name):
    
    if not sys.warnoptions: import warnings; warnings.simplefilter('ignore')
    pd.set_option('display.max_rows',None); pd.set_option('display.max_columns',None)
    
    try:
        
        df = tabula.read_pdf(file_path,pages='all',multiple_tables = True)
        df_list = df
        
        col_list = ['Description','Narration','Remarks','Particulars','DESCRIPTION','Description','Description','PARTICULARS','Transaction Details','Narration','NARRATION','PERTICULERS','Details of transaction','ransaction Remarks','Transaction\rParticulars','Transaction Description','ransaction Remarks','Account Description','NARATION','Narration Chq/Ref No','Deposits','Amount (Rs.)','Credit','CREDIT','Deposit Amt.','DEPOSIT','Deposit','Deposit Amount\r(INR )','Amount','Deposit Amt','Type','Deposit Balance','WithDrawal','Value','Credit (Rs.)','Withdrawal Amt. Deposit Amt.','Deposit Amount\r(INR )','Credit(Rs)','Withdrawals Deposits','Cr Amount','Withdrawal (Dr)/','Withdrawal Amt.','Withdrawal','Withdrawal','DEBIT','Withdrawals','Debit','Withdrawal (Dr)','Withdrawal Amt. Deposit Amt.','Withdrawal (Dr)/','Withdrawal Amount\r(INR )','Debit (Rs.)','Debit(Rs)','WITHDRAWALS','Withdrawal INR','Withdrawal Amt','Amount','Withdrawal Amount','Withdrawals Deposits','Dr Amount','Balance','Closing Balance','BALANCE','Running Balance','BALANCE','Balance (INR )','Amount','MODE**','Running','Balance(Rs)','Total Amount\rDr/Cr','Date','date','Transaction','Txn','Transaction Date','Debit/Credit','Transaction date','Txn Date','Tran Date','Balance (?)','Branch','Cheque No','Chq./Ref.','Entry Date','Cheque','TRANSACTION\rDATE','Trans Date','Tran Date','DATE','Post Date','Value\rDate','Date (Value\rDate)','Tran Date','Txn dt','Txn Dt','Value Date','Chq./Ref.No.','Value Dt','Chq\rNo.','Transaction Description','Total Amount\rDr/Cr','Debit (Rs.)','Credit (Rs.)','Balance (Rs.)','Dr Amount','Cr Amount','Instruments','Total Amou']
        
        date_list=['Date','date','Transaction','Txn','Transaction Date','Transaction date','Txn Date','Tran Date','Date','TRANSACTION\rDATE','Trans Date','Tran Date','DATE','Post Date','Value\rDate','Date (Value\rDate)','Txn dt','Txn Dt','Value Date']
        
        narration_list = ['Description','Narration','Details','Remarks','Particulars','DESCRIPTION','Description','Description','PARTICULARS','Transaction Details','Narration','NARRATION','PERTICULERS','Details of transaction','ransaction Remarks','Transaction\rParticulars','Transaction Description','ransaction Remarks','Account Description','NARATION','Narration Chq/Ref No']
        
        credit_list = ['Deposits','Amount (Rs.)','Credit','CREDIT','Deposit Amt.','DEPOSIT','Deposit','Deposit Amount\r(INR )','Amount','Credit (Rs.)','Deposit Amount\r(INR )','Credit(Rs)','Withdrawals Deposits','Cr Amount','Withdrawal (Dr)/','DEPOSITS','WITHDRAWALS']
        
        debit_list = ['Withdrawal Amt.','Withdrawal','Withdrawal','DEBIT','Withdrawals','Debit','Withdrawal (Dr)','Withdrawal Amt. Deposit Amt.','Withdrawal (Dr)/','Withdrawal Amount\r(INR )','Debit (Rs.)','Debit(Rs)','WITHDRAWALS','Withdrawal INR','Withdrawal Amt','Amount','Withdrawal Amount', 'Withdrawals Deposits','WithDrawal','Dr Amount']
        
        balance_list = ['Balance','Closing Balance','BALANCE','Running Balance','BALANCE','Balance (INR )','Amount','Running','Balance(Rs)','Total Amount\rDr/Cr']
        
        UPI=["UPI","upi","Upi"]
        
        widrawal = ["WD","ATM","ATW","WITHDRAWAL"]

        Salary=["Salary","SALARY","salary","SAL","Sal","BULK","bulk","Bulk","PAYROLL","payroll","CCT"]

        NACH = ["ACH","EMI","MANDATE DEBIT"]
        
        NACH_Bounce = ["RTN","ECS","RETURN","Return","Bounce","EMI RTN","Ecs","ecs"]
        
        E_Commerse = ["AMAZO","Amazon","Flipkar","AMZN","myntra","Amazon","ECOM","MYNTRA","Myntra","Ajio","Pharmeasy","ajio","AJIO","PHARMEASY","Nykaa","NYKAA","nykaa","Snapdeal","SNAPDEAL","FLIPKAR","Pepperfry","pepperfry","PREPPERFY","Meesho","MEESHO","meesho",]
        
        Online_Grosery =["Spar","SPAR","spar","BigBasket","bigbasket","BIGBASKET","big-basket","Big-Basket","BIG-BASKET","Grofers","GROFERS","grofers","JioMart","JIOMART","dunzo","DUNZO","ZEOPT","zepto","Blinkit","blinkit","BLINKIT","Zepto"]
        
        Online_FOOD=["Zomat","Swigg","ZOMAT","zomat","swigg","UberEats","ubereats","UBEREATS","Food Panda","FOOD PANDA","FOOD","Domino","DOMINO","domino"]
        
        Btting_sites = ["bet365","BET365","Betway","BETWAY","betway","10Cric","10cric","Parimatch","PARIMATCH","parimatch","LeoVegas","LEOVEGAS","leovegas","Comeon","COMEON","cameon","4rabet","4RABET","Fun88","FUN88","fun88","22Bet","22BET","22bet","1xBet","1xbet","1xBET"]
        
        Gambling_sites = ["Hobi Games","HOBI","Hobi","Rummy","RUMMY","rummy","Teen Patti","TEEN PATTI","teen patti","A23","ACE2","Ace2"]

        test_data = df_list[0]
        col_len = test_data.shape[1]
        tab_cols = test_data.columns; table_columns = []
        row_index = []
        try:    
            table_columns = unknown_columns(tab_cols,col_list)
        except:
            resp = jsonify({'status':'failed', 'message' : 'pdf not readable, Uploaded file must be pdf'})
            resp.status_code = 400
            return resp

        uc_count = op.countOf(table_columns,'Unknown_column')

        if uc_count >= 3 or len(table_columns)<=3:
            for row_ind in range(col_len-1):
                test_list = list(test_data[tab_cols[row_ind]])
                for i in range(len(col_list)):
                    col_el = col_list[i]
                    if col_el in test_list: row_inde = test_list.index(col_el); row_index.append(row_inde)
            
            if len(row_index) == 0:
                lst_no = 0 if len(df_list) <= 4 else 4; data1 = df_list[1]; data2 = df_list[2]; data3 = df_list[lst_no]
                data1_columns = []; data2_columns = []; data3_columns = []; 
                
                page_data1 = data1.values.tolist(); page_data2 = data2.values.tolist(); page_data3 = data3.values.tolist(); 
                data1_cols = data1.columns; data2_cols = data2.columns; data3_cols = data3.columns; 
                
                data1_columns = unknown_columns(data1_cols,col_list); data1_count = op.countOf(data1_columns,'Unknown_column')
                data2_columns = unknown_columns(data2_cols,col_list); data2_count = op.countOf(data1_columns,'Unknown_column')
                data3_columns = unknown_columns(data3_cols,col_list); data3_count = op.countOf(data1_columns,'Unknown_column')
                
                data_uc_count = [data1_count,data2_count,data3_count]; min_uc_index = data_uc_count.index(min(data_uc_count))
                dict_cols = {0:data1_columns,1:data2_columns,2:data3_columns}; dict_data = {0:data1,1:data2,2:data3}
                data_tab_cols = dict_cols[min_uc_index]; data_first = dict_data[min_uc_index]; page_data0 = data_first.values.tolist()
                pdf_data = []
                pdf_data = pdf_data + page_data0 + page_data1 + page_data2 + page_data3
                
                for ls in range(len(df_list)): page_data = df[ls].values.tolist(); pdf_data = pdf_data + page_data
                data1_pdf = pd.DataFrame(pdf_data); repete = data1_pdf.shape[1]-len(data_tab_cols)
                
                for _ in range(repete): data_tab_cols.append('column_added')
                pdf_data = pd.DataFrame(pdf_data,columns = data_tab_cols); data_pdf = pdf_data.replace(np.nan,''); com_table = data_pdf; new_com_table = data_pdf
            
            elif min(row_index) >= 2:
                test_data1 = test_data.values.tolist(); row_value = min(row_index); data_col_list = test_data1[row_value] + test_data1[row_value+1]; columns_list=[]; row_columns=[]
                for elem in range(len(data_col_list)): list_txt = list(str(data_col_list[elem]).split()); columns_list = columns_list + list_txt
                
                for elem in range(len(columns_list)):
                    if columns_list[elem] in col_list: col_name = columns_list[elem]; row_columns.append(col_name)
                data1 = df_list[1]; data1 = data1.values.tolist()
                
                for lst_len in range(len(df_list)): page_data = df_list[lst_len]; page_data = page_data.values.tolist(); data1 = data1 + page_data
                pdf_data1 = pd.DataFrame(data1); repete = pdf_data1.shape[1]-len(row_columns)
                
                for _ in range(repete): row_columns.append('column_added')
                pdf_data = pd.DataFrame(data1,columns = row_columns); pdf_data = pdf_data.replace(np.nan,''); com_table = pdf_data; new_com_table = pdf_data
            
            else: data_pdf = tables(df,df_list); com_table = data_pdf.rename(columns = data_pdf.iloc[0]).drop(data_pdf.index[0]);new_com_table=data_pdf.rename(columns=data_pdf.iloc[1]).drop(data_pdf.index[1])
        
        else: data_pdf = tables(df,df_list); com_table = data_pdf.rename(columns=data_pdf.iloc[0]).drop(data_pdf.index[0]); new_com_table = data_pdf.rename(columns=data_pdf.iloc[1]).drop(data_pdf.index[1])

        def column_serch():
            tab_col = []
            col_ind_list=[]
            for j in range(len(list(com_table.columns))):
                test=[]
                com_tab_list = com_table[list(com_table.columns)[j]]
                for i in range(len(list(com_table[list(com_table.columns)[0]]))):
                    com_cell = com_tab_list[i]
                    cell_len= len(str(com_cell))
                    test.append(cell_len)
                avg = sum(test)/len(test)
                col_ind_list.append(avg)
                tab_col.append(avg)
                test.clear()
            index=[]
            colum=["Debit","Credit","Balance"]
            for ind in range(len(col_ind_list)):
                if col_ind_list[ind] >=9 and col_ind_list[ind] <= 11:
                    date_ind=ind
                if col_ind_list[ind] == max(col_ind_list):
                    nar_ind=ind
                if col_ind_list[ind] >=0.7 and col_ind_list[ind] <= 8:
                    for m in range(3):
                        index[ind]=colum[m]
            if len(index)==3:
                credit_ind=index[0]
                debit_ind=index[1]
                balance_ind=index[2]
            elif len(index)==2:
                credit_ind=index[0]
                debit_ind=index[0]
                balance_ind=index[1]
            col_index={"date_ind":date_ind,"nar_ind":nar_ind,"credit_ind":credit_ind,"debit_ind":debit_ind,"balance_ind":balance_ind}   
        
            return col_index

        cols = list(com_table.columns); cols1 = list(new_com_table.columns); 
        for i in range(len(cols)): 
            if cols[i] in date_list:date_ind=i
        for j in range(len(cols1)):
            if cols1[j] in date_list:date_ind=j
        for k in range(len(cols)):
            if cols[k] in narration_list:nar_ind=k
        for l in range(len(cols1)):
            if cols1[l] in narration_list:nar_ind=l
        for m in range(len(cols)):
            if cols[m] in credit_list:credit_ind=m 
        for n in range(len(cols1)):
            if cols1[n] in credit_list:credit_ind=n 
        for dbt in range(len(cols)):
            if cols[dbt] in debit_list:debit_ind=dbt
        for dbt1 in range(len(cols1)):
            if cols1[dbt1] in debit_list:debit_ind=dbt1
        for blns in range(len(cols)):
            if cols[blns] in balance_list:balance_ind=blns
        for blns1 in range(len(cols1)):
            if cols1[blns1] in balance_list:balance_ind=blns1 
        try:            
            Transaction_date =list(com_table[cols[date_ind]])
            Narration = list(com_table[cols[nar_ind]])
            Deposits=list(com_table[cols[credit_ind]])
            Debit = list(com_table[cols[debit_ind]])
            Balance = list(com_table[cols[balance_ind]])

        except:
            col_index = column_serch()
            Transaction_date =list(com_table[cols[col_index["date_ind"]]])
            Narration = list(com_table[cols[col_index["nar_ind"]]])
            Deposits=list(com_table[cols[col_index["credit_ind"]]])
            Debit = list(com_table[cols[col_index["debit_ind"]]])
            Balance = list(com_table[cols[col_index["balance_ind"]]])

        
        trans_data = pd.DataFrame(Transaction_date,columns = ['Transaction Date']); nar_data = pd.DataFrame(Narration,columns = ['Narration']); cred_data = pd.DataFrame(Deposits,columns = ['Credit']); debt_data = pd.DataFrame(Debit,columns = ['Debit']); bal_data = pd.DataFrame(Balance,columns = ['Balance'])
        data = trans_data.join(nar_data); data = data.join(cred_data); data = data.join(debt_data); data = data.join(bal_data); data = data.replace(np.nan,'')
        
        axis_list=['axis-bank','Axis Bank  India','Axis Bank  India','AXIS (UTI) Bank','Axis Bank India','Axis Bank, India','Axis Ban','Axis Bank','Axis Bank Ltd','Axis Bank Ltd.','Axis Bank ','Axis','axis','AXIS']
            
        if bank_name in axis_list:
            for ele in range(len(Narration)-1):
                if Transaction_date[ele] == '' and Balance[ele] == '': Narration[ele+1] = str(Narration[ele]) + str(Narration[ele+1])
        else:   
            for ele in range(len(Narration)):
                if Transaction_date[ele] == '': Narration[ele-1] = str(Narration[ele-1]) + str(Narration[ele])
        
        Transaction_date = pd.DataFrame(Transaction_date,columns = ['Transaction Date']); Narration = pd.DataFrame(Narration,columns = ['Narration']); Deposits = pd.DataFrame(Deposits,columns = ['Credit']); Debit = pd.DataFrame(Debit,columns = ['Debit']); Balance = pd.DataFrame(Balance,columns = ['Balance']); 
        data = Transaction_date.join(Narration); data = data.join(Deposits); data = data.join(Debit); data = data.join(Balance); txn_date = list(data['Transaction Date']); cr_list = list(data['Credit']); dr_list = list(data['Debit']); bls_list = list(data['Balance']); row_index = []
        
        for row_num in range(len(data['Narration'])):
            if txn_date[row_num] == '': a = row_num; row_index.append(a)
            elif cr_list[row_num] == '' and dr_list[row_num] == '' and bls_list == '': b = row_num; row_index.append(b)
        unique_row_index=[]
        
        for x in range(len(row_index)):
            if row_index[x] not in unique_row_index: row_ind = row_index[x]; unique_row_index.append(row_ind)
        data = data.drop(unique_row_index,axis=0); 
        data.reset_index(inplace = True)
        data = data.drop("index",axis=1)
        output = []
        Transaction_Date = list(data["Transaction Date"])
        Narration = list(data["Narration"])
        Credit = list(data["Credit"])
        Debit = list(data["Debit"])
        Balance = list(data["Balance"])
        batch_id = uuid.uuid1()

        for info in range(len(Transaction_Date)):
            txn = Transaction_Date[info]
            narr = Narration[info]
            cred = Credit[info]
            deb = Debit[info]
            bal = Balance[info]

            bal=string_float(bal)
            deb=string_float(deb)
            cred=string_float(cred)

            if bal == 0:
                bal=deb
                deb=cred
                cred=0.0
                
            try:
                if deb>cred:
                    rmk = "Debit"
                    
                elif cred>deb:
                    rmk = "Credit"
                else:
                    rmk=np.nan
            except:
                rmk=np.nan                
            txn_count= {"transactionNumber":info,"dateTime":txn,"description":narr,"Credit":cred,"batchID":batch_id,
            "Debit":deb, "balanceAfterTransaction":bal,"category":np.nan,
            "transactionId":uuid.uuid1(),"bank":bank_name,"remark":np.nan,"type":rmk}
            output.append(txn_count)
            for carr in range(len(output)):
                serch=str(output[carr]["description"])
                for upi in range(len(UPI)):
                    upi_serch=str(UPI[upi])
                    if re.findall(upi_serch, serch):output[carr]["category"] = "UPI"
                for wt in range(len(widrawal)):
                    wt_serch=str(widrawal[wt])
                    if re.findall(wt_serch, serch):output[carr]["category"] = "ATM Withdrawal"
                if re.findall("NEFT", serch):output[carr]["category"] = "NEFT"                 
                for sal in range(len(Salary)):
                    sal_serch=str(Salary[sal])
                    if re.findall(sal_serch, serch):output[carr]["category"] = "Salary"
                for nach in range(len(NACH)):
                    nach_serch=str(NACH[nach])
                    if re.findall(nach_serch, serch):output[carr]["category"] = "NACH"
                for bnach in range(len(NACH_Bounce)):
                    bnach_serch=str(NACH_Bounce[bnach])
                    if re.findall(bnach_serch, serch):output[carr]["category"] = "NACH_Bounce"
                for ecom in range(len(E_Commerse)):
                    ecom_serch=str(E_Commerse[ecom])
                    if re.findall(ecom_serch, serch):output[carr]["category"] = "E_Commerse"
                for gross in range(len(Online_Grosery)):
                    gross_serch=str(Online_Grosery[gross])
                    if re.findall(gross_serch, serch):output[carr]["category"] = "Online_Grosery"
                for food in range(len(Online_FOOD)):
                    food_serch=str(Online_FOOD[food])
                    if re.findall(food_serch, serch):output[carr]["category"] = "Online_FOOD"
                for bet in range(len(Btting_sites)):
                    bet_serch=str(Btting_sites[bet])
                    if re.findall(bet_serch, serch):output[carr]["category"] = "Beting_sites"
                for fan in range(len(Gambling_sites)):
                    fan_serch=str(Gambling_sites[fan])
                    if re.findall(fan_serch, serch):output[carr]["category"] = "Fantacy_Gamming" 
                if re.findall("RAZOR", serch):output[carr]["category"] = "RAZORPAY"
                if re.findall("RZP", serch):output[carr]["category"] = "RAZORPAY"
                if re.findall("INB", serch):output[carr]["category"] = "INTERNET BANKING TRANSACTION" 
                if re.findall("RENT", serch):output[carr]["category"] = "RENT"
                if re.findall("bill", serch):output[carr]["category"] = "BILL PAYMENT"   
                if re.findall("BILL", serch):output[carr]["category"] = "BILL PAYMENT" 
                if re.findall("POS ", serch):output[carr]["category"] = "Card Transaction" 
                if re.findall("debit card", serch):output[carr]["category"] = "Card Transaction"
                if re.findall("CHQ DEP", serch):output[carr]["category"] = "CHQ DEP" 
                if re.findall("IMPS", serch):output[carr]["category"] = "IMPS"
                          
        return output
    

    except:
        resp = jsonify({'status':'failed', 'message' : 'pdf not readable'})
        resp.status_code = 400
        return resp
    