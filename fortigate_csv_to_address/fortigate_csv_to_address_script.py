N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_address_output.txt', 'w') as f:
	f.write('')

### Append first line to output
with open('fortigate_csv_to_address_output.txt', 'a') as f:
    f.write('config firewall address' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_address_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # address
        col1 = values[1].replace(N, '') # subnet
        col2 = values[2].replace(N, '') # comment
        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_address_output.txt', 'a') as f:
                f.write('edit ' +  Q + col0 + Q + N)
                f.write('set subnet ' + Q + col1 + Q + N)
                f.write('set comment ' + Q + col2 + Q + N)
                f.write('next' + N)     
        row = row + 1       

### Append and 'end' to the output
with open('fortigate_csv_to_address_output.txt', 'a') as f:
    f.write('end' + N)