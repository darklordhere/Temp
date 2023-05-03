import pandas as pd

class validateEmail:
    def validate(email):
        x=email.split("@")
        if len(x)==2:
            domain=['gmail.com',"outlook.com","example.com","example.net"]
            if x[-1] in domain:
                if len(x[0]) != 0:
                    return True
                else:
                    return False
            else:
                return False
            
        else:
            return False

df = pd.read_csv('emails.csv')

validate_email = validateEmail.validate

df['valid'] = ''

valid_count = 0 # Counter for valid email addresses

for index, row in df.iterrows():
    print(f"Checking email {index+1}")
    if validate_email(row['email']):
        df.at[index, 'valid'] = 'valid'
        valid_count += 1
    else:
        df.at[index, 'valid'] = 'invalid'

df_valid = df.loc[df['valid'] == 'valid']
df_valid.to_csv('output.csv', index=False)

print(f"\n{valid_count} out of {len(df)} email addresses are valid.")

print("Done.")
