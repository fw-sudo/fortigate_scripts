N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_vips_output.txt', 'w') as f:
	f.write('')

### Append first line to output
with open('fortigate_csv_to_vips_output.txt', 'a') as f:
    f.write('config firewall vip' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_vips_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # vip
        col1 = values[1].replace(N, '') # extip
        col2 = values[2].replace(N, '') # mappedip
        col3 = values[3].replace(N, '') # protocol
        col4 = values[4].replace(N, '') # extport
        col5 = values[5].replace(N, '') # mappedport
        col6 = values[6].replace(N, '') # comment

        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_vips_output.txt', 'a') as f:
                f.write('edit ' + Q + col0 + Q + N)
                f.write('set portforward enable' + N)
                f.write('set extip ' + Q + col1 + Q + N)
                f.write('set mappedip ' + Q + col2 + Q + N)
                f.write('set protocol' + Q + col3 + Q + N)
                f.write('set extport ' + Q + col4 + Q + N)
                f.write('set mappedport ' + Q + col5 + Q + N)
                f.write('set comment ' + Q + col6 + Q + N)
                f.write('next' + N)     
        row = row + 1       

### Append and 'end' to the output
with open('fortigate_csv_to_vips_output.txt', 'a') as f:
    f.write('end' + N)