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
                "course_code": "CSC1113",
                "course_title": "Foundation of Computer Science",
                "year": 1,
                "semester": 1,
                "description": """{
  "Introduction to Computer Systems": {
    "Evolution of Computers": "Overview of the historical development of computers from early mechanical devices to modern systems.",
    "Classification of Modern Computers": "Categorization of computers based on size, capability, and usage, such as supercomputers, mainframes, personal computers, and embedded systems."
  },
  "Representation of Data": {
    "Number Systems": "Study of different number systems like binary, decimal, octal, and hexadecimal used in computing.",
    "Binary Arithmetic": "Operations such as addition, subtraction, multiplication, and division in binary.",
    "Signed Integer Representation": "Methods to represent positive and negative integers, including sign-magnitude, one’s complement, and two’s complement.",
    "Floating Point Representation": "Representation of real numbers in computers using floating-point notation, including IEEE 754 standard."
  },
  "Computer Hardware": {
    "Input/Output Devices": "Devices for user interaction with computers, such as keyboards, mice, monitors, and printers.",
    "CPU Organization": "Structure and functioning of the Central Processing Unit, including ALU, control unit, and registers.",
    "Storage Devices": "Primary and secondary storage devices like RAM, hard drives, SSDs, and optical media.",
    "Expansion Cards and System Interfaces": "Components like graphics cards, sound cards, and interfaces such as USB, PCIe, and SATA."
  },
  "Computer Software": {
    "Operating Systems": "Software that manages hardware and provides services for applications, e.g., Windows, Linux, macOS.",
    "Utility Programs": "Tools for system maintenance, such as antivirus software, disk defragmenters, and backup utilities.",
    "Application Software": "Programs designed for end-users, including word processors, browsers, and games.",
    "Concepts of Programming": "Fundamentals of writing code, including algorithms, data structures, and programming paradigms.",
    "Web-based, Desktop, and Mobile Applications": "Differences and characteristics of applications designed for web browsers, desktop environments, and mobile devices."
  },
  "Computer Network": {
    "Use of Network": "Purpose and applications of networks for communication, resource sharing, and data transfer.",
    "Communication Media": "Wired (e.g., Ethernet, fiber optics) and wireless (e.g., Wi-Fi, Bluetooth) media for data transmission.",
    "Network Devices": "Hardware like routers, switches, hubs, and access points used in networking.",
    "Types of Networks": "Classification of networks like LAN, WAN, MAN, PAN, and VPN based on scope and functionality."
  },
  "System Maintenance and Troubleshooting": {
    "PC Maintenance Tools": "Software and hardware tools for maintaining system performance, such as diagnostic utilities and cleaning kits.",
    "Troubleshooting Guidelines": "Systematic approaches to diagnose and resolve hardware and software issues.",
    "Upgrading a System": "Procedures for upgrading hardware components (e.g., RAM, CPU) and software updates."
  },
  "Practical": {
    "Basic Commands of Windows and Linux": "Introduction to command-line operations in Windows (e.g., CMD, PowerShell) and Linux (e.g., Bash).",
    "Introduction to Word Processing": "Basics of creating and editing documents using software like Microsoft Word or Google Docs.",
    "Spreadsheet Software": "Fundamentals of spreadsheet applications like Microsoft Excel or Google Sheets for data organization and analysis.",
    "Presentation Software": "Creating and managing presentations using tools like Microsoft PowerPoint or Google Slides."
  }
}""",
  "credit_value": 3},
{
  "course_code": "CSC1123",
  "course_title": "Introduction to Programming",
  "year": 1,
  "semester": 1,
  "description": """ 
  {
  "Introduction to Computer Systems": {
    "Evolution of Computers": "Overview of the historical development of computers from early mechanical devices to modern systems.",
    "Classification of Modern Computers": "Categorization of computers based on size, capability, and usage, such as supercomputers, mainframes, personal computers, and embedded systems."
  },
  "Representation of Data": {
    "Number Systems": "Study of different number systems like binary, decimal, octal, and hexadecimal used in computing.",
    "Binary Arithmetic": "Operations such as addition, subtraction, multiplication, and division in binary.",
    "Signed Integer Representation": "Methods to represent positive and negative integers, including sign-magnitude, one’s complement, and two’s complement.",
    "Floating Point Representation": "Representation of real numbers in computers using floating-point notation, including IEEE 754 standard."
  },
  "Computer Hardware": {
    "Input/Output Devices": "Devices for user interaction with computers, such as keyboards, mice, monitors, and printers.",
    "CPU Organization": "Structure and functioning of the Central Processing Unit, including ALU, control unit, and registers.",
    "Storage Devices": "Primary and secondary storage devices like RAM, hard drives, SSDs, and optical media.",
    "Expansion Cards and System Interfaces": "Components like graphics cards, sound cards, and interfaces such as USB, PCIe, and SATA."
  },
  "Computer Software": {
    "Operating Systems": "Software that manages hardware and provides services for applications, e.g., Windows, Linux, macOS.",
    "Utility Programs": "Tools for system maintenance, such as antivirus software, disk defragmenters, and backup utilities.",
    "Application Software": "Programs designed for end-users, including word processors, browsers, and games.",
    "Concepts of Programming": "Fundamentals of writing code, including algorithms, data structures, and programming paradigms.",
    "Web-based, Desktop, and Mobile Applications": "Differences and characteristics of applications designed for web browsers, desktop environments, and mobile devices."
  },
  "Computer Network": {
    "Use of Network": "Purpose and applications of networks for communication, resource sharing, and data transfer.",
    "Communication Media": "Wired (e.g., Ethernet, fiber optics) and wireless (e.g., Wi-Fi, Bluetooth) media for data transmission.",
    "Network Devices": "Hardware like routers, switches, hubs, and access points used in networking.",
    "Types of Networks": "Classification of networks like LAN, WAN, MAN, PAN, and VPN based on scope and functionality."
  },
  "System Maintenance and Troubleshooting": {
    "PC Maintenance Tools": "Software and hardware tools for maintaining system performance, such as diagnostic utilities and cleaning kits.",
    "Troubleshooting Guidelines": "Systematic approaches to diagnose and resolve hardware and software issues.",
    "Upgrading a System": "Procedures for upgrading hardware components (e.g., RAM, CPU) and software updates."
  },
  "Practical": {
    "Basic Commands of Windows and Linux": "Introduction to command-line operations in Windows (e.g., CMD, PowerShell) and Linux (e.g., Bash).",
    "Introduction to Word Processing": "Basics of creating and editing documents using software like Microsoft Word or Google Docs.",
    "Spreadsheet Software": "Fundamentals of spreadsheet applications like Microsoft Excel or Google Sheets for data organization and analysis.",
    "Presentation Software": "Creating and managing presentations using tools like Microsoft PowerPoint or Google Slides."
  }
}""",
"credit_value":3},
{
  "course_code": "ACU1113",
  "course_title": "English Language I",
  "year": 1,
  "semester": 1,
  "description": """ 
  {
  "Reading": {
    "Reading Skills": "Techniques to improve comprehension and speed when reading texts.",
    "Identifying Main Points": "Recognizing key ideas and themes in a passage or text.",
    "Understanding Vocabulary": "Decoding and interpreting words in context to enhance comprehension."
  },
  "Writing": {
    "Introducing the Mechanics of Writing": "Fundamentals of grammar, punctuation, and sentence structure.",
    "Introducing Vocabulary in and Around the University Environment": "Learning academic and campus-related terminology.",
    "Developing Sentences and Paragraphs": "Crafting coherent and cohesive sentences and paragraphs.",
    "Transferring Graphic, Pictorial Information into Writing": "Describing charts, graphs, or images in written form.",
    "Preparing to Write an Essay or a Project": "Planning and organizing content for essays or academic projects."
  },
  "Speaking": {
    "Describing Objects": "Explaining the characteristics, functions, or appearance of objects clearly.",
    "Interviewing": "Conducting and responding to interviews with effective communication.",
    "Giving Instructions": "Providing clear, step-by-step directions or guidance.",
    "Making Short Speeches": "Delivering concise, structured oral presentations."
  },
  "Listening": {
    "Listening to Discriminate Sounds": "Identifying and distinguishing specific sounds or phonetic elements.",
    "Listening for Specific Information": "Focusing on key details or data in spoken content.",
    "Listening and Responding to Telephone Conversation": "Understanding and engaging in phone-based communication effectively."
  },
  "Language Structures": {
    "Introducing Structures": "Learning fundamental grammatical structures for effective communication.",
    "Question Formation": "Constructing different types of questions (e.g., yes/no, wh-questions).",
    "Articles": "Using definite (the) and indefinite (a/an) articles appropriately.",
    "Prepositions": "Understanding and applying prepositions for time, place, and direction.",
    "Pronouns": "Using personal, possessive, reflexive, and relative pronouns correctly.",
    "Quantifiers": "Applying terms like some, any, much, many, and few to indicate quantity.",
    "Word Class": "Identifying and using parts of speech (nouns, verbs, adjectives, adverbs, etc.).",
    "Active and Passive": "Understanding and using active and passive voice constructions.",
    "Topics to Be Selected from Student’s Field of Interest": "Exploring language structures relevant to students' academic or personal interests.",
    "Submission of Individual Projects": "Completing and presenting individual assignments based on learned concepts."
  }
}""",
"credit_value": 3}
        
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