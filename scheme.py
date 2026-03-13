from models import Scheme

SCHEMES = [
    Scheme(
        id=1,
        name="Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
        description="Providing income support to all landholding farmers' families.",
        target_occupation="Farmer",
        benefits="Rs. 6000 per year"
    ),
    Scheme(
        id=2,
        name="Sukanya Samriddhi Yojana",
        description="Targeted at the parents of girl children to build a fund for their future education and marriage.",
        required_age_max=10,
        target_gender="Female",
        benefits="High interest rate tax-free savings account"
    ),
    Scheme(
        id=3,
        name="Ayushman Bharat Yojana",
        description="Health insurance scheme for economically weaker sections.",
        max_income=250000,
        benefits="Health cover of Rs. 5 lakhs per family per year"
    ),
    Scheme(
        id=4,
        name="Stand-Up India Scheme",
        description="Facilitates bank loans for SC/ST and women borrowers for setting up a greenfield enterprise.",
        required_age_min=18,
        benefits="Bank loans between 10 lakh and 1 crore"
    )
]
