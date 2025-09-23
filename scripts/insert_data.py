# Import the database session and your model
from services.database import SessionLocal
from models.sql_models import Module  # Import your Subject model

def insert_some_modules():
    # Create a database session
    db = SessionLocal()
    
    try:
        # Define your dummy data - List of subjects for Computer Science
        modules = [
            {
                "course_code": "AMA1113",
                "course_title": "Differential Equations",
                "year": 1,
                "semester": 1,
                "description": """ {
  "differentialEquationsTopics": [
    {
      "id": 1,
      "title": "Introduction: Basic concepts of the differential equations",
      "description": "Fundamental concepts, definitions, and classification of differential equations including order, degree, and types of solutions."
    },
    {
      "id": 2,
      "title": "Equations of First Order and First Degree",
      "description": "Solution techniques for first-order ordinary differential equations.",
      "subtopics": [
        {
          "id": 2.1,
          "title": "Separable variables and reduction to separable variables",
          "description": "Methods for solving equations where variables can be separated on each side of the equation."
        },
        {
          "id": 2.2,
          "title": "Exact equations and those reducible to exact form",
          "description": "Techniques for identifying and solving exact differential equations using integrating factors."
        },
        {
          "id": 2.3,
          "title": "Linear equations and those reducible to linear forms",
          "description": "Solution methods for first-order linear differential equations and Bernoulli equations."
        },
        {
          "id": 2.4,
          "title": "Applications of First Order Differential Equations",
          "description": "Practical modeling of real-world phenomena using first-order ODEs."
        }
      ]
    },
    {
      "id": 3,
      "title": "Equations of First Order and Higher Degree",
      "description": "Solution methods for equations where the derivative appears to a higher power.",
      "subtopics": [
        {
          "id": 3.1,
          "title": "Linear differential equations with constant coefficients",
          "description": "Solving homogeneous and non-homogeneous linear ODEs with constant coefficients."
        },
        {
          "id": 3.2,
          "title": "Linear differential equations with variable coefficients",
          "description": "Solutions for equations where coefficients are functions of the independent variable."
        },
        {
          "id": 3.3,
          "title": "System of Linear Differential Equations",
          "description": "Techniques for solving sets of simultaneous linear differential equations."
        }
      ]
    },
    {
      "id": 4,
      "title": "Total Differential Equations",
      "description": "Methods for solving equations involving multiple differentials.",
      "subtopics": [
        {
          "id": 4.1,
          "title": "Conditions for integrability and exactness",
          "description": "Criteria for determining when a total differential equation is exact and integrable."
        },
        {
          "id": 4.2,
          "title": "Solving integrable Total Differential Equations",
          "description": "Techniques for finding solutions to exact total differential equations."
        }
      ]
    }
  ]
}"""},
{
    "course_code": "PMA1113",
    "course_title": "Foundation of Mathematics",
    "year": 1,
    "semester": 1,
    "description": """{
  "discreteMathematicsTopics": [
    {
      "id": 1,
      "title": "Foundations of Sets",
      "description": "Fundamental concepts and operations of set theory.",
      "subtopics": [
        {
          "id": 1.1,
          "title": "Basic notation",
          "description": "Standard symbols and terminology used in set theory."
        },
        {
          "id": 1.2,
          "title": "Representations and examples",
          "description": "Different ways to represent sets including roster, set-builder, and Venn diagram methods."
        },
        {
          "id": 1.3,
          "title": "Membership and subsets",
          "description": "Concepts of element membership and subset relationships between sets."
        },
        {
          "id": 1.4,
          "title": "Operations on sets",
          "description": "Union, intersection, difference, and complement operations."
        },
        {
          "id": 1.5,
          "title": "Cartesian products",
          "description": "Formation of ordered pairs and n-tuples from multiple sets."
        },
        {
          "id": 1.6,
          "title": "Power sets",
          "description": "The set of all subsets of a given set."
        },
        {
          "id": 1.7,
          "title": "Cardinality",
          "description": "The number of elements in a set and comparison of set sizes."
        },
        {
          "id": 1.8,
          "title": "Infinite sets",
          "description": "Sets with unlimited elements and their properties."
        }
      ]
    },
    {
      "id": 2,
      "title": "Relations and Functions",
      "description": "Study of relationships between sets and functional mappings.",
      "subtopics": [
        {
          "id": 2.1,
          "title": "Domain and range of a relation",
          "description": "Input and output sets for relations between sets."
        },
        {
          "id": 2.2,
          "title": "One-to-one, one-to-many, many-to-one relations",
          "description": "Classification of relations based on element mappings."
        },
        {
          "id": 2.3,
          "title": "Inverse relations",
          "description": "Reversal of ordered pairs in a relation."
        },
        {
          "id": 2.4,
          "title": "Reflexive, symmetric, and transitive relations",
          "description": "Properties that define equivalence relations."
        },
        {
          "id": 2.5,
          "title": "Into, Onto, One-one, and bijective functions",
          "description": "Classification of functions based on their mapping properties."
        }
      ]
    },
    {
      "id": 3,
      "title": "Propositional and Predicate Logic",
      "description": "Formal systems for representing and reasoning about logical statements.",
      "subtopics": [
        {
          "id": 3.1,
          "title": "Propositions",
          "description": "Declarative statements that are either true or false."
        },
        {
          "id": 3.2,
          "title": "Quantifiers",
          "description": "Universal and existential quantifiers in logical expressions."
        },
        {
          "id": 3.3,
          "title": "Predicates",
          "description": "Statements containing variables that become propositions when values are substituted."
        },
        {
          "id": 3.4,
          "title": "Proofs",
          "description": "Methods for establishing the truth of mathematical statements."
        }
      ]
    },
    {
      "id": 4,
      "title": "Boolean Algebra and Logic Gates",
      "description": "Algebraic structure for logical operations and their implementation in digital circuits.",
      "subtopics": [
        {
          "id": 4.1,
          "title": "Introduction",
          "description": "Basic concepts and axioms of Boolean algebra."
        },
        {
          "id": 4.2,
          "title": "Duality",
          "description": "Principle that Boolean expressions have dual forms with interchanged AND/OR operators and 0/1 values."
        },
        {
          "id": 4.3,
          "title": "Representation theorem",
          "description": "Fundamental theorem showing how Boolean functions can be represented in canonical forms."
        },
        {
          "id": 4.4,
          "title": "Sum-of-products",
          "description": "Standard form for representing Boolean functions as OR of AND terms."
        },
        {
          "id": 4.5,
          "title": "Combinatorial circuits",
          "description": "Digital circuits whose output depends only on current inputs."
        },
        {
          "id": 4.6,
          "title": "Boolean Functions",
          "description": "Functions that operate on binary inputs and produce binary outputs."
        },
        {
          "id": 4.7,
          "title": "Karnaugh map and applications",
          "description": "Graphical method for simplifying Boolean expressions."
        }
      ]
    },
    {
      "id": 5,
      "title": "Group Theory",
      "description": "Algebraic study of symmetry and mathematical structures with a single binary operation.",
      "subtopics": [
        {
          "id": 5.1,
          "title": "Definitions and examples",
          "description": "Basic concepts of groups with illustrative examples."
        },
        {
          "id": 5.2,
          "title": "Order of elements",
          "description": "The smallest positive integer such that applying the group operation to an element that many times yields the identity."
        },
        {
          "id": 5.3,
          "title": "Sub-groups",
          "description": "Subsets of groups that themselves form groups under the same operation."
        },
        {
          "id": 5.4,
          "title": "Cosets and Lagrange's theorem",
          "description": "Decomposition of groups into subsets and the theorem relating orders of groups and subgroups."
        },
        {
          "id": 5.5,
          "title": "Cyclic groups",
          "description": "Groups that can be generated by a single element."
        }
      ]
    }
  ]
}""",
    "credit_value": 3
},
{
    "course_code": "STA1113",
    "course_title": " Introduction to Statistics",
    "year": 1,
    "semester": 1,
    "description": """{
  "statisticsTopics": [
    {
      "id": 1,
      "title": "Descriptive Statistics",
      "description": "Methods for summarizing and describing the main features of datasets.",
      "subtopics": [
        {
          "id": 1.1,
          "title": "Introduction",
          "description": "Overview of descriptive statistics and their role in data analysis."
        },
        {
          "id": 1.2,
          "title": "Quantitative measures",
          "description": "Numerical values that summarize and describe characteristics of data."
        },
        {
          "id": 1.3,
          "title": "Variables",
          "description": "Types of variables in statistical analysis (categorical, numerical, discrete, continuous)."
        },
        {
          "id": 1.4,
          "title": "Central tendency",
          "description": "Measures that identify the center of a dataset (mean, median, mode)."
        },
        {
          "id": 1.5,
          "title": "Variability",
          "description": "Measures that quantify the spread or dispersion of data points."
        },
        {
          "id": 1.6,
          "title": "Measures of location",
          "description": "Quantiles, percentiles, and other positional measures in a dataset."
        }
      ]
    },
    {
      "id": 2,
      "title": "Charts and Graphs",
      "description": "Visual representations of data patterns and distributions.",
      "subtopics": [
        {
          "id": 2.1,
          "title": "Patterns in data",
          "description": "Identifying trends, clusters, and other patterns through visualization."
        },
        {
          "id": 2.2,
          "title": "Dot plots",
          "description": "Simple graphs displaying individual data points along a number line."
        },
        {
          "id": 2.3,
          "title": "Histograms",
          "description": "Bar graphs representing the frequency distribution of continuous data."
        },
        {
          "id": 2.4,
          "title": "Stemplots",
          "description": "Also called stem-and-leaf plots, showing data distribution while preserving raw values."
        },
        {
          "id": 2.5,
          "title": "Box plots",
          "description": "Graphical display of data distribution through quartiles and outliers."
        },
        {
          "id": 2.6,
          "title": "Ogives",
          "description": "Cumulative frequency graphs showing the running total of frequencies."
        },
        {
          "id": 2.7,
          "title": "Scatterplots",
          "description": "Graphs displaying the relationship between two quantitative variables."
        }
      ]
    },
    {
      "id": 3,
      "title": "Measures of Dispersion",
      "description": "Statistical measures that describe how spread out or varied a dataset is.",
      "subtopics": [
        {
          "id": 3.1,
          "title": "Skewness",
          "description": "Measure of the asymmetry of the probability distribution of a real-valued random variable."
        },
        {
          "id": 3.2,
          "title": "Coefficient of skewness",
          "description": "Numerical measure of the degree of asymmetry of a distribution."
        },
        {
          "id": 3.3,
          "title": "Kurtosis",
          "description": "Measure of the 'tailedness' of the probability distribution of a real-valued random variable."
        }
      ]
    },
    {
      "id": 4,
      "title": "Probability",
      "description": "Mathematical framework for quantifying uncertainty and randomness.",
      "subtopics": [
        {
          "id": 4.1,
          "title": "Introduction",
          "description": "Basic concepts and definitions of probability theory."
        },
        {
          "id": 4.2,
          "title": "Axiomatic probability",
          "description": "Formal mathematical foundation of probability based on Kolmogorov's axioms."
        },
        {
          "id": 4.3,
          "title": "Conditional probability",
          "description": "Probability of an event given that another event has occurred."
        },
        {
          "id": 4.4,
          "title": "Bayes' Theorem",
          "description": "Formula that describes how to update the probabilities of hypotheses based on evidence."
        },
        {
          "id": 4.5,
          "title": "Independence",
          "description": "Concept of events that do not influence each other's probabilities."
        },
        {
          "id": 4.6,
          "title": "Combinatorial methods",
          "description": "Counting techniques used in probability calculations (permutations, combinations)."
        }
      ]
    },
    {
      "id": 5,
      "title": "Random Variables",
      "description": "Variables whose values are determined by random phenomena and their probability distributions.",
      "subtopics": [
        {
          "id": 5.1,
          "title": "Discrete and continuous random variables",
          "description": "Classification of random variables based on their possible values."
        },
        {
          "id": 5.2,
          "title": "Expectation and variance",
          "description": "Mean (expected value) and measure of spread for random variables."
        },
        {
          "id": 5.3,
          "title": "Joint and conditional distributions",
          "description": "Probability distributions involving multiple random variables and their relationships."
        },
        {
          "id": 5.4,
          "title": "Moment generating functions",
          "description": "Special functions that generate moments of probability distributions."
        },
        {
          "id": 5.5,
          "title": "Probability generating functions",
          "description": "Functions used primarily for discrete random variables to generate probabilities."
        },
        {
          "id": 5.6,
          "title": "Binomial, Poisson, Uniform, and Normal distributions",
          "description": "Fundamental probability distributions with wide applications in statistics."
        },
        {
          "id": 5.7,
          "title": "Student's t-distribution",
          "description": "Probability distribution used when estimating the mean of a normally distributed population with small sample sizes."
        }
      ]
    }
  ]
}""",
    "credit_value": 3
}
        
        ]

        # Insert each subject
        for subject_data in modules:
            # Create a new Subject object
            module = Module(**subject_data)
            
            # Add to the session
            db.add(module)
        
        # Commit all changes to the database
        db.commit()
        print(f"✅ Successfully inserted {len(modules)} records!")
        
    except Exception as e:
        # If anything goes wrong, rollback the changes
        db.rollback()
        print(f"❌ Error inserting data: {e}")
        raise e
        
    finally:
        # Always close the session
        db.close()

if __name__ == "__main__":
    insert_some_modules()