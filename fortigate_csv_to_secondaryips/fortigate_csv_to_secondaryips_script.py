N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_secondaryips_output.txt', 'w') as f:
	f.write('')

### Append first line to output
#with open('fortigate_csv_to_secondaryips_output.txt', 'a') as f:
#    f.write('' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_secondaryips_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # port
        col1 = values[1].replace(N, '') # secondaryip
        col2 = values[2].replace(N, '') # allowaccess
        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_secondaryips_output.txt', 'a') as f:
                f.write('config system interface' +  N)
                f.write('edit ' + col0 + N)
                f.write('set secondary-IP enable' + N)
                f.write('config secondaryip' + N)
                f.write('edit 0' +  N)
                f.write('set ip ' + col1 + N)
                f.write('set allowaccess ' + col2 + N)
                f.write('end' + N)
                f.write('end' + N) 
        row = row + 1       

### Append and 'end' to the output
#with open('fortigate_csv_to_secondaryips_output.txt', 'a') as f:
#    f.write('end' + N)