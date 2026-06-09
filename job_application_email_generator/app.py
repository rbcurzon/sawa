import pyperclip
import argparse

def format_words(words):
    string_splits = words.split()
    return' '.join([word.capitalize() for word in string_splits])

parser = argparse.ArgumentParser(description="Simple email generator for applying job.")
parser.add_argument('hr_name', help='The name of hiring manager.')
parser.add_argument('position', help="The position you're applying")
parser.add_argument('company_name',help="The name of the company")
parser.add_argument('platform', help='The platform where you found the position.')
args = parser.parse_args()
HR_NAME = format_words(args.hr_name)
POSITION_APPLYING = format_words(args.position).upper()
COMPANY_NAME = format_words(args.company_name).upper()
PLATFORM_APPLICATION_POSTED = format_words(args.platform)


EMAIL = f'''
Dear {HR_NAME},

I am writing to express my interest in the {POSITION_APPLYING} position at {COMPANY_NAME} as advertised on {PLATFORM_APPLICATION_POSTED}.

I have attached my resume for your review. I believe my background and skills would make me a strong candidate for this role, and I am eager to contribute to your team.

Thank you for your time and consideration. I look forward to hearing from you soon.

Best regards,

Ronald Curzon
09281651160
curzonronald@gmail.com
'''

pyperclip.copy(EMAIL)
print('Your can now paste your email.')
