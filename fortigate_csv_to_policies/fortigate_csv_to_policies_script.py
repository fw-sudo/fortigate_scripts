N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_policies_output.txt', 'w') as f:
	f.write('')

### Append first line to output
with open('fortigate_csv_to_policies_output.txt', 'a') as f:
    f.write('config firewall policy' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_policies_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # id
        col1 = values[1].replace(N, '') # status
        col2 = values[2].replace(N, '') # name
        col3 = values[3].replace(N, '') # srcintf
        col4 = values[4].replace(N, '') # dstintf
        col5 = values[5].replace(N, '') # srcaddr
        col6 = values[6].replace(N, '') # dstaddr
        col7 = values[7].replace(N, '') # service
        col8 = values[8].replace(N, '') # action
        col9 = values[9].replace(N, '') # schedule
        col10 = values[10].replace(N, '') # nat
        col11 = values[11].replace(N, '') # ippool
        col12 = values[12].replace(N, '') # poolname
        col13 = values[13].replace(N, '') # logtraffic
        col14 = values[14].replace(N, '') # comment
        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_policies_output.txt', 'a') as f:
                f.write('edit ' + Q + col0 + Q + N)
                f.write('set status ' + Q + col1 + Q + N)
                f.write('set name ' + Q + col2 + Q + N)
                f.write('set srcintf ' + Q + col3 + Q + N)
                f.write('set dstintf ' + Q + col4 + Q + N)
                f.write('set srcaddr ' + Q + col5 + Q + N)
                f.write('set dstaddr ' + Q + col6 + Q + N)
                f.write('set service ' + Q + col7 + Q + N)
                f.write('set action ' + Q + col8 + Q + N)
                f.write('set schedule ' + Q + col9 + Q + N)
                f.write('set nat ' + Q + col10 + Q + N)
                f.write('set ippool ' + Q + col11 + Q + N)
                f.write('set poolname ' + Q + col12 + Q + N)
                f.write('set logtraffic ' + Q + col13 + Q + N)
                f.write('set comment ' + Q + col14 + Q + N)
                f.write('next' + N)     
        row = row + 1       

### Append and 'end' to the output
with open('fortigate_csv_to_policies_output.txt', 'a') as f:
    f.write('end' + N)