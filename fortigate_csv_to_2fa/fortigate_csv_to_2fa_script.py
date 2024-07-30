N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_2fa_output.txt', 'w') as f:
	f.write('')

### Append first line to output
with open('fortigate_csv_to_2fa_output.txt', 'a') as f:
    f.write('config user local' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_2fa_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # user
        col1 = values[1].replace(N, '') # email
        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_2fa_output.txt', 'a') as f:
                f.write('edit ' +  Q + col0 + Q + N)
                f.write('set two-factor email' + N)
                f.write('set email-to ' + Q + col1 + Q + N)
                f.write('next' + N)     
        row = row + 1       

### Append and 'end' to the output
with open('fortigate_csv_to_2fa_output.txt', 'a') as f:
    f.write('end' + N)