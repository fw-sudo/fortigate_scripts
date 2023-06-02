N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_dhcp-reservation_output.txt', 'w') as f:
	f.write('')

### Append first line to output
#with open('fortigate_csv_to_dhcp-reservation_output.txt', 'a') as f:
#    f.write('config reserved-address' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_dhcp-reservation_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # dhcpserver
        col1 = values[1].replace(N, '') # mac
        col2 = values[2].replace(N, '') # ip
        col3 = values[3].replace(N, '') # description
        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_dhcp-reservation_output.txt', 'a') as f:
                f.write('config system dhcp server' + N)
                f.write('edit ' + col0 + N)
                f.write('config reserved-address' + N)
                f.write('edit 0' + N)
                f.write('set mac ' + Q + col1 + Q + N)
                f.write('set ip ' + Q + col2 + Q + N)
                f.write('set description ' + Q + col3 + Q + N)
                f.write('end' + N)
                f.write('end' + N)   
        row = row + 1       

### Append and 'end' to the output
#with open('fortigate_csv_to_dhcp-reservation_output.txt', 'a') as f:
#    f.write('end' + N)