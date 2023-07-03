from bs4 import BeautifulSoup
import requests
import time

def find_jobs():

	html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
	soup = BeautifulSoup(html_text, "lxml")
	jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

	for index, job in enumerate(jobs):

		published_date = job.find("span", class_ = "sim-posted").span.text.strip()

		if published_date == "Posted few days ago":

			company_name = job.find("h3", class_ = "joblist-comp-name").text.strip()
			skills = job.find("span", class_ = "srp-skills").text.lower().strip()
			more_info = job.header.h2.a["href"]
			
			if unfamiliar_skill not in skills:

				with open(f"./jobs/{index}.txt", 'w') as f:

					f.write(f"COMPANY NAME: {company_name}\n")
					f.write(f"REQUIRED SKILLS: {skills}\n")
					f.write(f"MORE INFO: {more_info}\n")

				print(f"File saved: {index}.txt\n")
				
print("\nThis project is running in", __name__, "\n")

if __name__ == "__main__":
	
	print("Enter any skill you are not familiar with")
	unfamiliar_skill = input("> ")
	print(f"Filtering out {unfamiliar_skill}\n")


	while True:

		find_jobs()
		time_wait = 10
		print(f"Waiting {time_wait} mintues...")
		time.sleep(time_wait * 60)