N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output CSV file
with open('fortigate_routes_to_csv_output.csv', 'w') as f:
	f.write('')

### Append first line to output CSV file
with open('fortigate_routes_to_csv_output.csv', 'a') as f:
    f.write('edit;dst;gateway;device;comment' + N)

### Read input txt and assign each row to a variable
with open('fortigate_routes_to_csv_input.txt', 'r') as f:
    for line in f:
    
        line = line.replace(N, '')      # Delete new list
        line = line.replace('    ', '') # Delete concatenation
        
        if line.find('edit ') != -1:
           col0 = (line.replace('edit ', ''))
           #col0 = (Q + col0 + Q)
        
        if line.find('set dst ') != -1:
            col1 = (line.replace('set dst ', ''))
            #col1 = (Q + col1 + Q)
            
        if line.find('set gateway ') != -1:
            col2 = (line.replace('set gateway ', ''))
            #col2 = (Q + col2 + Q)
        
        if line.find('set device ') != -1:
            col3 = (line.replace('set device ', ''))
            #col3 = (Q + col3 + Q)
         
        if line.find('set device ') != -1:
            col4 = (line.replace('set device ', ''))
            #col4 = (Q + col4 + Q)
            
        if line.find('set comment ') != -1:
            col5 = (line.replace('set comment ', ''))
            #col5 = (Q + col5 + Q)
        
        # When 'next' appears concatenate all variables and append to the CSV
        if line.find('next') != -1:       
            with open('fortigate_routes_to_csv_output.csv', 'a') as f:
                f.write(col0 + ';' + col1 + ';' + col2 + ';' + col3 + ';' + col4 + ';' + col5 + N)
            
