# Import the database session and your model
from services.database import SessionLocal
from models.sql_models import Module  # Import your Subject model
def insert_some_modules():
    # Create a database session
    db = SessionLocal()
    db.expire_all() 
    
    try:
        # Define your dummy data - List of subjects for Computer Science
        modules = [
            {
                "course_code": "AMA2213",
                "course_title": "Mechanics",
                "year": 2,
                "semester": 2,
                "description": """Introduction: Kinematics, Dynamics and statics, Foundation of mechanics and mathematical models, Newton’s laws, Force and mass, Work, Power, Kinetic energy, Conservative force field, Potential energy, Conservation of energy, Impulse, Conservation of momentum and non-conservative forces. Motion in a uniform field: Uniformly accelerated motion, Freely falling bodies, Potential and potential energy in a uniform force field, Motion in a resisting medium, Pulley motion and inclination motion. Harmonic Oscillator: Simple harmonic oscillator, Amplitude, period and frequency of simple harmonic motion, Energy of a simple harmonic oscillator, Damped harmonic oscillator, Over-damped, Critically damped and under-damped motion, Simple pendulum. Gravitation: Basic concepts of gravitation and formulas, Field and potential, Rocket motion, Equation of rocket motion, Relative-motion analysis. Motion of a particle on a curve: Motion of a particle on a smooth vertical curve, Tangential equation of the motion, Normal equation of the motion. Flexible chains and strings: Catenary, Equation of common catenary, Cartesian equation of common catenary, Properties of catenary, Equations of equilibrium of a string, Catenary of uniform strength. Shear force and Bending moment: Types of beams and loads, Internal stress in a rigid body, Concentrated and distributed forces, Relationship between bending moment and shearing force and Diagrams.""",
                "credit_value":3},
            {
                "course_code": "STA2213",
                "course_title": "Sampling Theory",
                "year": 2,
                "semester": 2,
                "description": """Introduction: Population, Sample, Sampling Design, Estimators. Simple Random Sampling: Simple Random Sampling With Replacement, Simple Random Sampling Without Replacement, Estimation of population mean and total under SRS, Determination of sample size under SRS, Estimation of Population Proportion. Stratified Sampling: Estimation of population mean and total under Stratified Sampling, Determination of sample size under Stratified Sampling, Allocations. Ratio estimator: Bias and Mean Square Error, Estimation of Variance, Confidence Interval, Ratio Estimator in Stratified Random Sampling. Difference estimator and Regression estimator: Difference Estimator, Difference Estimator in Stratified Random Sampling, Regression Estimator, Regression Estimators in Stratified Sampling. Systematic Sampling: Estimation of population mean and total under Systematic Sampling, Comparison of Systematic Sampling, Simple Random Sampling and Stratified Random Sampling for Different Types of Populations, Circular Systematic Sampling. Cluster Sampling: Estimation of Population Mean, Estimation of Efficiency by a Cluster Sample.""",
                "credit_value":3},
            {
                "course_code": "CSC2212",
                "course_title": "Data Comm & Networks",
                "year": 2,
                "semester": 2,
                "description": """Introduction: Data Communication concepts, Networks, Internet, Protocols and Standards, Topology, Transmission mode, Categories of network, Applications. Signals: Periodic and aperiodic signals, Analog signals, Time and frequency domains, Frequency spectrum and bandwidth, Digital signals, Analog and digital data. Network Models: Layered Task, OSI Model, TCP/IP Model. Transmission Media: Guided media, Unguided media, Transmission impairment, Signal propagation, Digital Modulation and Multiplexing. Network Devices: NIC, Switches, Bridges, Hub and Routers, network design and implementation.""",
                "credit_value":2},
            {
                "course_code": "CSC2222",
                "course_title": "Software Eng",
                "year": 2,
                "semester": 2,
                "description": """Software Processes: Introduction to software process models, Activities within software life-cycles, Evaluation of software process models. Requirements Engineering: Properties of requirements, Software requirements elicitation, Describing system data, Functional requirements, Non-functional requirements. Software Design: Design Models, class, architectural and interface designs. Different types of architecture, levels of abstraction, separation of concerns, information hiding, coupling and cohesion, re-use of standard structures. Software Testing: Verification and validation concepts, Testing types, Testing fundamentals. Unit, integration, validation, and system testing, Test plan creation and test case generation, Black-box and white-box testing techniques. Software Evolution: Software development in the context of large, pre-existing code bases, Software change, Refactoring, Software evolution, Characteristics of maintainable software, Re-engineering systems, Software reuse.""",
                "credit_value":2},
            {
                "course_code": "CSC2234",
                "course_title": "Numerical Computing",
                "year": 2,
                "semester": 2,
                "description": """Error analysis: Computer number representation, round off errors, truncation errors, loss of significance. Solution of equation of one variable: Bisection method, the method of false-position, fixed point iteration, convergence of iterative methods, Aiken’s ∆2 process, order of convergence, Newton-Raphson method, convergence of Newton-Raphson iteration, Secant method, Order of Secant method. Roots of Polynomials: Computing with polynomials, Newton method to compute the roots of a polynomial, Muller’s method, Bairstow’s method for quadratic factors. Interpolation: Interpolation and Lagrange polynomial, Errors in Interpolation, Divided Difference, Interpolation with equally spaced points, Interpolation with cubic spline. Numerical Differentiation: Numerical Differentiation, Derivatives from difference table, Derivation of derivative formula using Lagrange’s Interpolation formula, Richardson’s Extrapolation, five point’s formula. Numerical Integration: Trapezodial Rule and Simpon’s Rule, Round off error in Trapezodial Rule and Simpon’s Rules, adaptive quadrature method, Gaussian quadrature. Numerical solution of system of linear equation: Direct method: Gaussion Elimination, pivoting strategies, operational count, Matrix factorization, compact schemes (Crouts, Choleski), Tridiagonal system, stability and Ill conditioning, Vector and matrix norms, condition number. Jacobi, Gauss-Seidal methods, Convergence of Iteration methods, Successive over relaxation method, Krylov subspace and conjugate gradient methods. Solution of Ordinary Differential Equations: Derivation of method, One step method, Runge-Kutta (R-K) method, Derivation of R-K methods, Euller’s method and Errors Estimation, Linear Multistep methods, Adams methods and predictor-corrector methods, Stability of Numerical methods. Practical: Practical implementation of the above concepts using Mathematical software.""",
                "credit_value":4},
            {
                "course_code": "ACU2212",
                "course_title": "Comm & Soft Skills",
                "year": 2,
                "semester": 2,
                "description": """Introduction: Communication and soft skills, Patterns and process, Downward and Upward communication, Horizontal and vertical communication, One-way and two-way communication, Multi-directional communication, Communications for Management, Efficiency in communication. Forms and Levels: Oral and written communication, Verbal and non-verbal communication, Para-language Code, Signals, Symbols, Icons, Gestures, Active Listening and Speaking, Writing for your people, Publishing and Editing, Inter personal communication, Public communication. Planning and Organization of communication: Establishment of Objective, Information search, Identification, Collection, Organization and presentation, Analytical skills, Resource allocation, Delegation, Timing, Coordination. Motivational Communication: Motivation, Instrumental and inspirational, Internal and external, Instructions, Reporting, Recommendations, Performance Appraisal and Styles of Control. Staffing and Leadership: Interview Techniques, Communication in Training, Development, Feedback, and Industrial Relations, Supportive Leadership, Directive leadership, Achievement Oriented leadership and Participative leadership. Public Relations, Marketing Communication: Negotiating and conflict resolution skills: Opening the process, Negotiations types, Conduct of Negotiation and problem solving skills, balancing personal and professional life, Communication during Negotiations, Bargaining, Teamwork, Flexibility and adaptation, Time management, Decisiveness, Responsibility and Accountability.""",
                "credit_value":0}
           
        
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