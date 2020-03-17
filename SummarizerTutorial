import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

text_str = '''
E-4B National Airborne Operations Center (NAOC)
Low Frequency Transmit System (LFTS) Trainer
Performance-Based Work Statement (PWS)
E4B-PWS-FY19-20
10 January 2020

Scope
Title
E-4B Aircraft Low Frequency Transmit System (LFTS) Trainer
Background
The E-4B mission suite has been modified to incorporate new LFTS long wire operations.  To capitalize on historical lessons learned and promote future growth, a training system will be provided.  This training system will allow for full operations and maintenance training on the LFTS system with no impact to aircraft availability. 
Task Description
The LFTS Trainer will facilitate training of the LFTS system for mission crew familiarization, operations and procedural scenarios, and maintenance troubleshooting and repairs. The trainer will allow for the development and execution of operational scenarios with the ability to assess individual responses and promote crew interaction through simulated operations. The trainer will provide the ability to demonstrate normal and degraded operations through instructor generated fault insertion and mission events. While the initial delivery encompasses the modification affected by LFTS, as the E-4B mission systems evolve, the trainer will keep pace with all modifications to maintain crew readiness and capability, as well as maximize operational aircraft availability.
Additionally, the goal is to create a virtual trainer that can be quickly reconfigured with software changes vice hardware modifications.  With the elimination of hardware dependencies, system availability is increased, and total life cycle costs are reduced.
Objective
The Contractor shall develop, manufacture/procure, test, document and deliver an E-4B LFTS Trainer that:
•	Shall give Air Force or Contractor instructors an interactive system to train LFTS operators and maintenance personnel.
•	Shall support continuous training through all phases to include annual training certification.
The contractor shall accomplish all tasks in order to provide the Government engineering and technical support to the E-4B program that addresses the requirements throughout this section (1.4) and in Section 3 of this document.
Hardware/Configuration
System
The LFTS Trainer configuration shall support four (4) trainee locations and two (2) instructor positions.  All trainer system hardware:
•	Shall consist of Commercial Off-the-Shelf, non-proprietary items to allow sustainment flexibility. 
•	Shall be of an appropriate size to support physically or through emulation the operations environment (E-4B 7.17 Console Station).
•	Shall support clear visual definition without pixelization or blurring.
•	Shall be a standalone system.
•	Shall support updates to applications, operating systems, and security environment through removable media (optical discs or console port).
•	Shall be compatible with aircrew personal headset interconnections.
The trainee consoles:
•	Shall emulate the E-4B 7.17 console station 
•	Shall place the trainee in the same approximate physical position and posture as in the aircraft.
•	Shall include all indicators, switches, and panels in aircraft representative locations.
•	Shall include virtual operator interfaces for all subsystems to include power control (circuit breakers). 
•	Shall support exporting of the emulated environment in a standalone format to enable students to gain familiarity in other computing environments such as a Computer Based Training Lab.
Facility
The LFTS Trainer should not require extensive facility modifications or its own dedicated facility for operation or storage.  This trainer will be employed in an office environment with standard ceilings, doors and floors. The LFTS Trainer:
•	Shall be capable of being housed inside a typical office space.
•	Shall consist of components capable of being moved through a standard 80” tall by 36” wide door. 
•	Shall operate on standard 110/220V 60Hz power. 
•	Shall not exceed a room footprint of 500 sq ft.
•	Shall include an Uninterruptable Power Supply (UPS) to enable graceful shutdown of the system server/s.
Training 
Training shall emulate the controls, switches, instrumentation, displays, and mission systems, along with their correct functionality and performance characteristics and be representative to the aircraft in location, function, and representation in order to train all tasks based on actual procedures as documented in the published E-4B technical data.
LFTS training sessions:
•	Shall replicate operation of the aircraft in normal, degraded, and emergency modes.
•	Shall include simulation modes for preflight, airborne mission, and post flight states.
•	Shall be capable of running a time-based scenario where discrete actions and inputs are injected based on a predetermined scenario or ad hoc by the instructor.
•	Shall be capable of injecting different faults, failures, and indications.
•	Shall be capable of capturing the configuration and settings of the Trainer in a “Snapshot” and utilize the Snapshot settings as an initial condition set for loading the Trainer.
•	Shall send and receive data between all trainee and instructor positions as well as other simulated crew positions and simulated ground observer.
•	Shall provide graphical displays to the instructor with situational awareness of the scenario as well as repeaters of the trainee panels/displays.
•	Shall be fully monitored and controlled by the instructor.
•	Shall support two simultaneous training sessions.
•	Shall permit review and replay of the training scenario, including audio communications to enable reconstruction for instructional purposes.
LFTS Training:
•	Shall include all operations functions for the LFTS wire operations based upon actual procedures as documented in the published E-4B technical data (operations and maintenance manuals).
•	Shall correlate the applicable visual and audio simulation scene during wire movement.
•	Shall display virtualized or previously recorded operation of reel and drogue that will react to and mirror the input of operator actions in real time.
•	Shall emulate LFTS connectivity and transmission of Emergency Action Messages (EAM) based upon the E-4B Message Processing System (MPS) Software.
The contract shall provide a priced option to run the MPS application as whole. 
 Referenced Documents
Government Documents
1.0	Other Documents
Government Furnished Property
The Contractor shall be responsible for the protection of all Government property in its possession. The Contractor shall maintain the systems, records, and methodologies necessary for effective control of Government property. The contractor is authorized the use of the GFP in their facility which is associated with this contract. The Contractor shall confirm and approve the final inventory with DCMA and a COR for all GFP.  (D018)
Quality Deficiency Reporting
The Contractor shall submit Quality Deficiency Reports IAW T.O. 00-35D-54 as required for GFE. (D017)
Commercial Off-The-Shelf Manuals and Associated Supplemental Data
The Contractor shall deliver manuals for Commercial Off-The-Shelf (COTS) items used to support the LFTS Trainer. (D015)
Requirements
Travel
The contractor may be required to travel to accomplish this requirement.
Program Management
The contractor shall perform administrative, technical, and financial management functions during the course of this effort and shall maintain a status of their effort towards achieving the PWS objectives; including all technical activities and efforts, problems/deficiencies, impacts, and recommended solutions. The contractor shall create an Integrated Master Schedule (IMS) upon start of program and provide to the Government no later than 45 business days after award. (D001). The Contractor shall ensure the IMS is structured with a time-phased Work Breakdown Structure down to two levels of detail below the critical path. The Work Breakdown Structure shall also include roles and responsibilities of the contract teamwork breakdown structure for the effort. The contractor shall create a Risk Management Plan and provide to the Government no later than 60 days after contract award. (D016) A recurring monthly status report assessing contract performance shall be provided by the contractor to the government, beginning 10 days after the first full month of performance. (D002)
Teleconferences
The contractor shall conduct bi-weekly teleconferences with the government to communicate updated status of programmatic activities.
Technical Interchange Meetings
The Contractor shall conduct two (2) Technical Interchange Meetings (TIMs), not exceed two (2) days, and be held at the contractors’ facilities unless otherwise directed by the Government. Agendas and minutes can be informal and provided in Contractor format. (D003, D004)
Technical Reviews
The contractor will provide the Government an agenda at least 5 calendar days prior to scheduled technical reviews. The contractor will record all decisions and actions items in the meeting minutes for each technical review. (D003, D004) The contractor shall perform the following program reviews.
Systems Requirements Review (SRR)
The Contractor will schedule and coordinate with the E-4B Program Office. The purpose of this meeting is to ensure all requirements are clearly understood and documented for the entire effort. The contractor shall perform an SRR based on the entry and exit criteria listed below:
Entry Criteria:
1.	Agenda and Presentation Package Provided
2.	Requirements Matrix (RM) Created
3.	PWS requirements captured in RM
4.	Derived requirements captured in RM 
Exit Criteria:
1.	Major SRR Action Items are closed.
2.	Contractor has demonstrated adequate understanding and progress on trainer requirements, system maintenance concept, functional analysis, significant system design criteria, systems engineering and test planning, system design documentation, and risk management of technical items.
3.	Contractor has set and will formally control the Functional Baseline
4.	Government has approved closure of the SRR.
The contractor shall adhere to the Entry and Exit Criteria for successful performance of this review.
Preliminary (PDR)
The contractor shall perform a PDR based on the entry and exit criteria listed below: 
Entry Criteria:
1.	Agenda and Presentation Package Provided
2.	System Block Diagram Developed
3.	Preliminary System Interfaces Defined
4.	Preliminary Mechanical and Electrical Design Available
5.	Proposed Design Solution meets/exceed requirements
6.	No outstanding CET deliverables from SRR
7.	Adequate copies of draft engineering drawings provided (the number of drawings for a PDR shall be a number agreed upon by the contractor and the Government prior to PDR).
8.	Draft copies of engineering drawings at 35% to 50% complete
9.	Drawing Tree (list of provided drawings) 
Exit Criteria:
1.	System Block Diagram is Acceptable
2.	Government concurrence on preliminary design
3.	Contractor control of Engineering Baseline demonstrated
4.	Risks acceptable and mitigation plans in place
5.	Government review and approval of the published PDR minutes
6.	Review of systems engineering
The contractor shall adhere to the Entry and Exit Criteria for successful performance of this review.
Critical Design Review (CDR)
The contractor shall perform a CDR based on the entry and exit criteria listed below: 
Entry Criteria:
1.	Agenda and Presentation Package Provided
2.	System Block Diagram Developed
3.	System Interfaces Defined
4.	Mechanical and Electrical Detailed Design Available
5.	Proposed Design Solution meets/exceed requirements
6.	Major SRR Action Items (AIs) closed
7.	No outstanding CET deliverables from PDR
8.	Adequate copies of draft engineering drawings provided (the number of drawings for CDR shall be a number agreed upon by the contractor and the Government at PDR).
9.	Draft copies of engineering drawings at 95% to 100% complete
10.	Updated Drawing Tree 
Exit Criteria:
1.	System Block Diagram is Acceptable
2.	Interfaces are defined
3.	Government concurrence on detailed design
4.	Contractor control of Engineering Baseline demonstrated
5.	Risks acceptable and mitigation plans in place
6.	Government review and approval of the published CDR minutes
7.	Detailed review of systems engineering including
The contractor shall adhere to the Entry and Exit Criteria for successful performance of this review.

Systems Engineering
The Contractor shall perform systems engineering IAW Institute of Electrical and Electronics Engineers (IEEE) 15288.1-2014.
Systems Engineering Management Plan (SEMP)
The Contractor shall develop, implement, and maintain a SEMP for the LFTS Trainer Program IAW IEEE 15288.1-2014. The SEMP shall address the overall approach of the Contractor’s technical management of the program. The Contractor’s SEMP shall be consistent with the Government’s LFTS Trainer Systems Engineering Plan (SEP)
Configuration Management
The contractor shall perform Configuration Management (CM), using MIL-HDBK-61A as a guide. The contractor shall develop and maintain a Configuration Management Plan (CMP) outlining the CM activities and methods to be utilized on the program and potential follow-on efforts. This plan shall define how the CM baselines will be established, controlled, and updated throughout the system lifecycle. (D009)
Software Development
The contractor shall develop any needed software to support the LFTS Trainer program.
Software Version Description Document (VDD)
Software VDD will be generated by the original equipment manufacturer (OEM) and submitted with the software release to the Government.
Cyber Security
The contractor shall be compliant with the overall LFTS Trainer cyber security accreditation.  The contractor shall provide source data / documentation. (ex: The accreditation credentials of the LFTS Trainer components). The government will work with accreditation authority to determine and facilitate any additional accreditation that may be required.  While the exact NIST controls are yet to be determined, the Contractor can expect an RMF categorization of L-L-L based on the LFTS Trainer being an unclassified standalone trainer not connected to any networks.  The government will update the Risk Management Framework’s (RMF) Control Set.
Cyber-Security Accreditation Support
The contractor shall support government Cyber-Security testing by providing answers to installation configuration questions from government personnel during the implementation and testing of the LFTS Trainer.
System Security Plan and Any Associated Plans of Action
The Contractor shall, upon request, provide to the government, a system security plan (or extract thereof) and any associated plans of action developed to satisfy the adequate security requirements of DFARS 252.204-7012, and in accordance with NIST Special Publication (SP) 800-171, “Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations” in effect at the time the solicitation is issued or as authorized by the contracting officer, to describe the contractor’s unclassified information system(s)/network(s) where covered defense information associated with the execution and performance of this contract is processed, is stored, or transmits. (D020)
The Contractor shall, upon request, provide the government with access to the system security plan(s) (or extracts thereof) and any associated plans of action for each of the Contractor’s tier one level subcontractor(s), vendor(s), and/or supplier(s), and the subcontractor’s tier one level subcontractor(s), vendor(s), and/or supplier(s), who process, store, or transmit covered defense information associated with the execution and performance of this contract. (D020)
Test
The contractor shall plan for, conduct, and support testing for the LFTS Trainer program. The contractor shall provide a Master Test Plan (MTP) that describes all testing to be accomplished. (D010) Testing
The testing for this project will be combined effort between the Government and the Contractor.  Regular periodic demonstrations of the software shall be conducted with the combined team to ensure the software development is meeting the Government’s expectations.  The Contractor shall employ Agile development methods to facilitate this requirement.  Hardware development will finish before software development so that in-plant testing of the LFTS Trainer can be conducted on the actual system.  Once in-plant testing is complete, the LFTS Trainer will be moved to its operational final location.  Once installed in the final Government facility, an operational checkout of the Trainer shall be conducted to ensure nothing degraded from in-plant testing.
The contractor shall support Government Acceptance Testing.  The Government will conduct in-plant and on-site test events to ensure that the Trainer meets the requirements.  In-plant testing with the Government will begin with a Warm-Start from a gold disc image. 
A Physical Configuration Audit (PCA) shall be conducted after installation onsite, to ensure the technical data package is accurate and that all physical hardware has been delivered and installed.  Once the LFTS Trainer has successfully completed an on-site operational checkout and PCA it will be ready for training.
Acceptance Test
The contractor shall deliver an Acceptance Test Procedure (ATP) for Government approval that verifies the LFTS Trainer functions as required at least 60 calendar days prior to delivery.
The ATP shall be performed with a Government witness to serve as Government verification that the installation is functional and all requirements have been met. (D010)
Test Reports
The contractor shall prepare and deliver a test report summarizing the results of the ATP. (D011)
Logistics Requirements
The contractor shall manage the appropriate logistics necessary to support LFTS Trainer development as well as facilitate activities to support testing.
Integrated Life Cycle Management (ILCM)
The contractor shall develop and maintain an ILCM using AFI 63-101/20-101 as a guideline. The ILCM shall include a supportability plan including the following:
1.	List of all items needed to build the LFTS Trainer 
2.	Reliability analysis to establish required spares levels
3.	Initial spares purchase recommendation
4.	Support Equipment
5.	
The contractor shall develop supportability data, in contractor format to define support equipment, and initial spares. (D012)
Technical Order (TO) Development Requirements: 
The Contractor shall develop and deliver technical manuals in accordance with TM-86-01Q - Air Force Technical Manual Contract Requirements (TMCR); reference TMCR for guidance. (D013)
Training
The Contractor shall train aircrew, maintenance personnel, and training instructors utilizing the standardized instructions necessary to acquire the knowledge and skills to execute developmental and operational test activities.  The Contractor shall train the personnel required to support the standup of the LFTS Trainer to prepare them to operate and maintain the trainer.  The Contractor shall provide support services for the LFTS Trainer as described in the following paragraphs.
Type 1 Training
The Contractor shall design, develop, test, deliver, and maintain Type 1 training materials.  The Contractor shall develop and provide Type 1 training to Government and government identified contractor personnel, and Government familiarization training IAW AETC Instruction (AETCI) 36-2219.  All Type 1 training products shall be provided to the Government as non-proprietary materials. The Contractor shall provide Type 1 training instructional materials that are concurrent with the system technical data.  The Contractor shall ensure that all Type 1 training materials are compliant with AETCI 36-2219, and incorporate AFMAN 36-2234 principles.  The Contractor shall deliver all Type 1 training materials to the Government, including outputs, rationale, and associated documentation resulting from the Instructional Systems Design (ISD) process used to generate the Type 1 training material. The Training Task List will be presented at the CDR for Government approval. The Contractor shall provide a final copy of all training materials to the E-4B Program Office 30 calendar days after the first training class is complete. (D014)
Transition Support
The Contractor shall, during the last ninety (90) days of period of performance from development to sustainment, provide support to the Government to ensure an orderly transition and minimize any impact on the operational readiness of the LFTS Trainer.  The Contractor shall conduct the transition such that disruption to ongoing training, training management, and support activities is minimized. The Contractor shall provide appropriate LFTS Trainer familiarization and instructor training based on existing training materials and on an as needed basis to ensure Government instructor training requirements are met.
Data Items
The following CDRLs apply to this delivery order and shall be submitted as described below. All data will be provided on the E-4B LFTS Trainer LCMP website.




'''


def _create_frequency_table(text_string) -> dict:
    """
    we create a dictionary for the word frequency table.
    For this, we should only use the words that are not part of the stopWords array.
    Removing stop words and making frequency table
    Stemmer - an algorithm to bring words to its root word.
    :rtype: dict
    """
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable


def _score_sentences(sentences, freqTable) -> dict:
    """
    score a sentence by its words
    Basic algorithm: adding the frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        word_count_in_sentence_except_stop_words = 0
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        if sentence[:10] in sentenceValue:
            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence_except_stop_words

        '''
        Notice that a potential issue with our score algorithm is that long sentences will have an advantage over short sentences. 
        To solve this, we're dividing every sentence score by the number of words in the sentence.
        
        Note that here sentence[:10] is the first 10 character of any sentence, this is to save memory while saving keys of
        the dictionary.
        '''

    return sentenceValue


def _find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = (sumValues / len(sentenceValue))

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary


def run_summarization(text):
    # 1 Create the word frequency table
    freq_table = _create_frequency_table(text)

    '''
    We already have a sentence tokenizer, so we just need 
    to run the sent_tokenize() method to create the array of sentences.
    '''

    # 2 Tokenize the sentences
    sentences = sent_tokenize(text)

    # 3 Important Algorithm: score the sentences
    sentence_scores = _score_sentences(sentences, freq_table)

    # 4 Find the threshold
    threshold = _find_average_score(sentence_scores)

    # 5 Important Algorithm: Generate the summary
    summary = _generate_summary(sentences, sentence_scores, 1.5 * threshold)

    return summary


if __name__ == '__main__':
    result = run_summarization(text_str)
    print(result)
