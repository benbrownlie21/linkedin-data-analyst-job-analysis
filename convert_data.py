import pandas as pd

df = pd.read_csv("C:\\Users\\bbrow\Downloads\\archive (1)\\postings.csv")


def categorize_experience(title):
    title = title.lower()
    if "Sr. Data Scientist" in title:
        return "Senior"
    elif "Retail Business Analyst - Target" in title:
        return "Mid"
    elif "Business Analyst - Healthcare (STAR CMS/HEDIS)" in title:
        return "Mid"
    elif "Unstructured Data Engineering Lead" in title:
        return "Senior"
    elif "\u200bData Engineer (Fabric)\u200b" in title:
        return "Mid"
    elif "DEI Business Analyst – Advisor Productivty Specialist" in title:
        return "Mid"
    elif "Clinical Data Scientist" in title:
        return "Mid"
    elif "Financial Analyst - 79476" in title:
        return "Mid"
    elif "Databricks Data Engineer" in title:
        return "Mid"
    elif "Enterprise Data Engineer" in title:
        return "Mid"
    elif "Senior Data Scientist for eComm Analytics" in title:
        return "Senior"
    elif "Sr. SAP SD/LE Business Analyst" in title:
        return "Senior"


def categorize_experience(title):
    title = title.lower()
    if "jr. data scientist (hybrid)" in title:
        return "Junior"
    elif (
        "people soft financials business analyst 3(only candidates  from texas)"
        in title
    ):
        return "Mid"
    elif "data engineer/scala developer" in title:
        return "Mid"
    elif "senior reporting analyst" in title:
        return "Senior"
    elif "senior business analyst, technology service management" in title:
        return "Senior"
    elif "intern-business analyst for it automation-nashville, tn-summer 2024" in title:
        return "Intern"
    elif "sr. data scientist (modeling)" in title:
        return "Senior"
    elif "business analyst ii ( 100% remote)" in title:
        return "Mid"
    elif "financial analyst i" in title:
        return "Mid"
    elif "senior financial analyst [hybrid]" in title:
        return "Senior"
    elif "data reporting analyst" in title:
        return "Mid"
    elif (
        "consultancy - education and data and analytics consultant, data and analytics team (dat), dapm nyhq (remote-based)"
        in title
    ):
        return "Mid"
    elif "data specialist i" in title:
        return "Mid"
    elif "master data specialist; training" in title:
        return "Mid"
    elif "senior financial reporting analyst ii, reinsurance" in title:
        return "Senior"
    elif "senior data scientist, google cloud support" in title:
        return "Senior"
    elif "principal data scientist - statistical programming" in title:
        return "Mid"
    elif "engineering manager - data engineering" in title:
        return "Manager"
    elif "principal data scientist - biostatistics" in title:
        return "Mid"
    elif "senior associate, data engineering - azure cloud" in title:
        return "Senior"
    elif "sr it data engineering associate" in title:
        return "Senior"
    elif "sr. data engineer(only w2)" in title:
        return "Senior"
    elif "data scientist (6+ years) (fulltime)" in title:
        return "Mid"
    elif "senior data engineer with python - w2" in title:
        return "Senior"
    elif "business analyst/product owner" in title:
        return "Mid"
    elif "marketing analyst - 79497" in title:
        return "Mid"
    elif "junior data engineer" in title:
        return "Junior"
    elif (
        "remote opportunity for p&c insurance data scientist/actuary - pr12690a"
        in title
    ):
        return "Mid"
    elif "investor relations marketing analyst" in title:
        return "Senior"
    elif "business analyst/product owner - crain’s best places to work" in title:
        return "Mid"
    elif "digital business analyst" in title:
        return "Mid"
    elif "senior data engineer, databricks" in title:
        return "Senior"
    elif "accounting systems business analyst" in title:
        return "Mid"
    elif "credit risk quantitative analyst" in title:
        return "Mid"
    elif "business analyst (hybrid schedule :: 2 days remote every week)" in title:
        return "Mid"
    elif "adobe data engineer || remote" in title:
        return "Mid"
    elif "data scientist iii, innovation" in title:
        return "Mid"
    elif "junior quantitative analyst, asset management" in title:
        return "Junior"
    elif "data engineer / power bi developer" in title:
        return "Mid"
    elif "adobe analytics consultant" in title:
        return "Mid"
    elif "proposal & technical marketing analyst – 100% remote" in title:
        return "Mid"
    elif "marketing analyst (c797)" in title:
        return "Mid"
    elif "sr. financial analyst (pharma)" in title:
        return "Senior"
    elif "financial analyst - multi-group physician practice" in title:
        return "Mid"
    elif "meteorological data scientist" in title:
        return "Mid"
    elif "data scientist, product analytics" in title:
        return "Mid"
    elif "accounting and business analyst" in title:
        return "Mid"
    elif "technical business analyst/project manager - compliance" in title:
        return "Manager"
    elif "data engineering lead (permanent direct hire)" in title:
        return "Senior"
    elif "technical business analyst (contract)" in title:
        return "Mid"
    elif "military fellowship - data scientist" in title:
        return "Mid"
    elif "financial analyst iv/v - lab support" in title:
        return "Mid"
    elif "financial analyst iii/iv - lab support" in title:
        return "Mid"
    elif "dod jr. financial analyst" in title:
        return "Mid"
    elif "business analyst, retirement & pension - consulting" in title:
        return "Mid"
    elif "senior business analytics & reporting analyst--operations" in title:
        return "Senior"
    elif "senior business analytics & reporting analyst--technology" in title:
        return "Senior"
    elif "senior financial analyst - utility rate analyst" in title:
        return "Senior"
    elif "sr. financial analyst - dealer" in title:
        return "Senior"
    elif "senior business analyst, retirement & pension - consulting" in title:
        return "Senior"
    elif (
        "senior financial analyst, technology business management - usa remote" in title
    ):
        return "Senior"
    elif "data scientist, marketing" in title:
        return "Mid"
    elif "senior financial analyst- diabetes operating unit" in title:
        return "Senior"
    elif "epm financial analyst i" in title:
        return "Mid"
    elif (
        "it - business analyst leader(electric distribution work management) remote contract w2 only"
        in title
    ):
        return "Senior"
    elif "principal data scientist (credit risk & decision science)" in title:
        return "Mid"
    else:
        if "senior" in title or "sr" in title:
            return "Senior"
        elif "junior" in title or "jr" in title:
            return "Junior"
        elif "manager" in title or "lead" in title or "head" in title:
            return "Management"
        else:
            return "Mid"


df["Experience"] = df["title"].apply(categorize_experience)


df.to_csv("C:\\Users\\bbrow\Downloads\\archive (1)\\postings2.csv", index=False)
print(df)
