# Package and Submission Workflow

## Table of Contents
1. [Overview](#overview)
2. [Package Types](#package-types)
3. [Package Structure](#package-structure)
4. [Package Creation Workflow](#package-creation-workflow)
5. [Submission Process](#submission-process)
6. [Package Status Lifecycle](#package-status-lifecycle)
7. [Version Control and Resubmission](#version-control-and-resubmission)
8. [Document Management](#document-management)
9. [Form Submissions](#form-submissions)
10. [Business Rules and Validations](#business-rules-and-validations)

---

## Overview

Packages are the core organizational unit in EPIC.submit. A package represents a complete submission to the EAO, containing all required documents, forms, and information for a specific submission type. This document explains how packages are created, managed, and submitted through their complete lifecycle.

### What is a Package?

A **package** is a structured container that organizes:
- Required documents (PDFs, spreadsheets, images)
- Structured form data (contact information, project details)
- Metadata (submission dates, contacts, references)
- Review history and status
- Communication between proponent and EAO

Think of a package as a digital filing cabinet where all materials for a specific submission are organized in a standardized way.

---

## Package Types

EPIC.submit supports three main package types, each serving a different regulatory purpose.

### 1. Management Plans (MP)

**Purpose:** Annual plans describing how the proponent will manage environmental aspects of their project.

**When Required:**
- Annually for active projects
- As specified in certificate conditions
- Before certain project phases begin

**Typical Contents:**
- **Project Overview**: Current project status and activities
- **Contact Information**: Key personnel and emergency contacts
- **Environmental Management**: Plans for air, water, waste, etc.
- **Monitoring Programs**: How environmental effects will be monitored
- **Adaptive Management**: How monitoring results will inform decisions
- **Compliance Summary**: Status of certificate condition compliance
- **Schedule**: Timeline for planned activities

**Business Context:**
Management plans are the primary mechanism for proponents to demonstrate ongoing compliance with their environmental certificate. They describe what the proponent will do in the coming year to protect the environment and meet certificate requirements.

**Submission Frequency:** Typically annual, but may vary by project

**Review Focus:** 
- Adequacy of environmental protection measures
- Compliance with certificate conditions
- Appropriateness of monitoring programs
- Feasibility of proposed activities

### 2. Independent Environmental Monitor (IEM) Reports

**Purpose:** Third-party verification that the proponent is complying with certificate conditions.

**When Required:**
- Quarterly during construction
- As specified in certificate conditions
- During high-risk project phases

**Typical Contents:**
- **Monitoring Activities**: What the IEM observed during the reporting period
- **Site Visits**: Summary of inspections conducted
- **Compliance Assessment**: Evaluation of adherence to conditions
- **Non-Compliance Issues**: Any violations or concerns identified
- **Recommendations**: Suggested improvements or corrective actions
- **Follow-up**: Status of previous recommendations

**Business Context:**
IEMs are independent professionals hired by the proponent but reporting to the EAO. They provide objective oversight of project activities and early identification of compliance issues. IEM reports give the EAO confidence that projects are being conducted as approved.

**Submission Frequency:** Quarterly or as required by certificate

**Review Focus:**
- Independence and objectivity of monitoring
- Thoroughness of site inspections
- Identification of compliance issues
- Adequacy of corrective actions

### 3. Consultation Records (CR)

**Purpose:** Documentation of Indigenous consultation activities and outcomes.

**When Required:**
- At consultation milestones
- Before major project decisions
- As required by consultation agreements
- When requested by Indigenous groups

**Typical Contents:**
- **Consultation Activities**: Meetings, correspondence, site visits
- **Issues Raised**: Concerns expressed by Indigenous groups
- **Proponent Responses**: How concerns were addressed
- **Agreements Reached**: Commitments and accommodations
- **Outstanding Issues**: Unresolved concerns
- **Next Steps**: Planned future consultation

**Business Context:**
Meaningful consultation with Indigenous peoples is a legal requirement and a key aspect of environmental assessment. Consultation records demonstrate that the proponent is fulfilling their consultation obligations and maintaining respectful relationships with Indigenous communities.

**Submission Frequency:** Milestone-based or as required

**Review Focus:**
- Meaningfulness of consultation
- Responsiveness to Indigenous concerns
- Fulfillment of consultation commitments
- Ongoing relationship maintenance

---

## Package Structure

Every package, regardless of type, follows a standardized structure to ensure consistency and completeness.

### Package Components

#### 1. Package Metadata

**Definition:** High-level information about the package itself.

**Includes:**
- Package name (e.g., "2024 Annual Management Plan")
- Package type (MP, IEM, CR)
- Associated project
- Reporting period (start and end dates)
- Primary contact person
- Submission date
- Version number

**Purpose:** Provides context and identification for the package.

#### 2. Items

**Definition:** Individual sections or requirements within a package.

**Characteristics:**
- Each item represents one specific requirement
- Items are predefined based on package type
- Each item has its own status
- Items can be completed independently
- Items may be mandatory or optional

**Example Items for Management Plan:**
- Project Overview (mandatory)
- Contact Information (mandatory)
- Air Quality Management (mandatory)
- Water Quality Management (mandatory)
- Wildlife Monitoring (mandatory)
- Adaptive Management Strategy (mandatory)
- Supporting Documentation (optional)

**Item Status:**
- **New**: Not yet started
- **In Progress**: Being worked on
- **Submitted**: Completed and submitted to EAO
- **Approved**: Accepted by EAO
- **Revision Required**: Needs changes

#### 3. Submissions

**Definition:** The actual content provided for each item.

**Two Types:**

**Document Submissions:**
- File uploads (PDF, Excel, Word, images)
- Multiple files can be uploaded per item
- Files can be replaced with newer versions
- Original files preserved in version history

**Form Submissions:**
- Structured data entry
- Predefined fields and formats
- Validation rules applied
- Data stored in database for reporting

**Versioning:**
- Each submission has a version number (e.g., 1.0, 1.1, 2.0)
- Major versions: Significant changes or resubmissions
- Minor versions: Small updates or corrections
- All versions retained for audit trail

#### 4. Package Status

**Definition:** Overall state of the package in the submission workflow.

**Key Statuses:**
- **New**: Just created, not yet submitted
- **Submitted**: Sent to EAO for review
- **Under Review**: Being evaluated by EAO staff
- **Approved**: Accepted by EAO
- **Revision Required**: Changes needed, resubmission required
- **Rejected**: Not accepted

**Status Array:**
Packages can have multiple statuses simultaneously (e.g., "Submitted" and "Under Consultation Check") to reflect different aspects of the review process.

---

## Package Creation Workflow

### Step 1: Initiate Package Creation

**User Action:**
1. Navigate to project dashboard
2. Click "Create New Package"
3. Select package type (MP, IEM, or CR)

**System Response:**
- Validates user has permission to create packages
- Checks that project is active and accessible
- Presents package creation form

**Business Rules:**
- User must have "Create Package" permission
- Project must be assigned to user's account
- Cannot create duplicate packages for same reporting period

### Step 2: Enter Package Metadata

**User Provides:**
- **Package Name**: Descriptive name (e.g., "Q1 2024 IEM Report")
- **Reporting Period**: Start and end dates for the submission
- **Primary Contact**: Person responsible for the submission
- **Additional Contacts**: Other key personnel
- **Reference Numbers**: Any relevant project or certificate numbers

**System Actions:**
- Validates required fields are completed
- Checks date ranges are logical
- Saves metadata

**Business Context:**
Metadata helps organize and identify packages, especially when organizations have multiple active projects and numerous submissions over time.

### Step 3: System Generates Items

**Automatic Process:**
- System looks up package type
- Retrieves template of required items for that type
- Creates item records for the package
- Sets initial status to "New" for all items
- Assigns sort order for logical presentation

**Example for Management Plan:**
1. Project Overview
2. Contact Information
3. Environmental Management Strategy
4. Air Quality Management
5. Water Quality Management
6. Wildlife Monitoring Program
7. Adaptive Management Approach
8. Compliance Summary
9. Supporting Documentation

**User Sees:**
- Checklist of items to complete
- Status indicator for each item
- Ability to click into each item to add content

**Business Benefit:**
Standardized item structure ensures nothing is missed and makes review more efficient.

### Step 4: Complete Items

**For Each Item, User Can:**

**Option A: Upload Documents**
1. Click "Upload Document"
2. Select file from computer
3. Add document description
4. Confirm upload

**Option B: Fill Out Forms**
1. Click "Fill Out Form"
2. Complete required fields
3. Save draft or submit

**Option C: Combination**
- Some items may require both documents and forms
- Complete all required components

**Progress Tracking:**
- System shows completion percentage
- Highlights incomplete items
- Allows saving work in progress
- Users can work on items in any order

**Collaboration:**
- Multiple users can work on different items simultaneously
- Changes are tracked by user
- Activity log shows who did what

### Step 5: Internal Review

**Before Submitting to EAO:**

**Self-Review:**
- User reviews all items for completeness
- Checks documents are correct and current
- Verifies form data is accurate
- Ensures all mandatory items are complete

**Team Review:**
- Share package with colleagues
- Gather feedback and make revisions
- Project Admin or Account Admin may review
- Address any internal concerns

**Quality Checks:**
- All required items completed
- Documents are readable and properly formatted
- Contact information is current
- Dates and references are correct

**Business Context:**
Internal review reduces the likelihood of EAO requesting revisions, saving time and ensuring quality submissions.

### Step 6: Submit to EAO

**User Action:**
1. Click "Submit to EAO"
2. Review submission checklist
3. Confirm submission

**System Validations:**
- All mandatory items must be complete
- At least one submission per mandatory item
- Package metadata is complete
- User has submission permission

**If Validation Fails:**
- System displays specific errors
- User must address issues before submitting
- Package remains in draft status

**If Validation Passes:**
- Package status changes to "Submitted"
- Submission timestamp recorded
- Confirmation email sent to submitter
- EAO staff notified of new submission
- Package locked from further editing (can only create new version)

**What User Receives:**
- Confirmation message on screen
- Email confirmation with submission details
- Reference number for tracking
- Expected timeline for review

---

## Submission Process

### Submission Types

#### Document Submissions

**Use Case:** When the requirement is best met with a file (report, plan, map, photo, spreadsheet).

**Process:**
1. User clicks "Upload Document" on an item
2. Selects file from computer
3. Optionally adds description
4. Confirms upload

**Supported File Types:**
- PDF (preferred for reports and plans)
- Microsoft Word (.docx)
- Microsoft Excel (.xlsx)
- Images (.jpg, .png)
- CAD files (for engineering drawings)
- Compressed files (.zip) for multiple related files

**File Size Limits:**
- Individual files: Up to 100 MB
- Total package size: Up to 1 GB
- Larger files require special arrangements

**Best Practices:**
- Use PDF for final documents
- Name files descriptively
- Include version numbers in filenames
- Compress large files when possible

**Version Control:**
- Each upload creates a new version
- Previous versions remain accessible
- Version history shows who uploaded when
- Can download any previous version

#### Form Submissions

**Use Case:** When structured data is needed (contacts, dates, numerical data, selections from lists).

**Process:**
1. User clicks "Fill Out Form" on an item
2. System displays form with fields
3. User enters data
4. System validates as user types
5. User saves draft or submits

**Field Types:**
- Text fields (names, descriptions)
- Number fields (quantities, measurements)
- Date fields (with calendar picker)
- Dropdown lists (predefined options)
- Checkboxes (yes/no, multiple selections)
- Text areas (longer descriptions)

**Validation:**
- Required fields must be completed
- Data formats must be correct (e.g., valid email)
- Number ranges enforced
- Date logic checked (end date after start date)

**Benefits:**
- Data can be searched and reported on
- Reduces errors from inconsistent formats
- Enables automated validation
- Facilitates data analysis

**Example: Contact Information Form**
```
Primary Contact Person
- Full Name: [text field]
- Title: [text field]
- Phone: [phone field with format validation]
- Email: [email field with validation]
- Address: [text area]

Emergency Contact
- Full Name: [text field]
- Phone: [phone field]
- Available 24/7: [yes/no checkbox]
```

### Submission Validation

**Automatic Checks:**

**Completeness:**
- All mandatory items have submissions
- Required form fields are filled
- Minimum number of documents met

**Format:**
- File types are allowed
- File sizes within limits
- Forms have valid data

**Business Rules:**
- Reporting period is logical
- Contacts are complete
- Dates are in correct sequence

**If Validation Fails:**
- Clear error messages displayed
- Specific items flagged
- User must correct before submission

**If Validation Passes:**
- Submission proceeds
- Package locked from editing
- Confirmation generated

---

## Package Status Lifecycle

### Status Flow Diagram

```
NEW
  ↓
SUBMITTED
  ↓
UNDER_REVIEW
  ↓
├─→ APPROVED (end state)
├─→ REJECTED (end state)
└─→ REVISION_REQUIRED
      ↓
    RESUBMITTED
      ↓
    (back to UNDER_REVIEW)
```

### Detailed Status Descriptions

#### 1. NEW

**Meaning:** Package created but not yet submitted to EAO.

**User Can:**
- Edit all items
- Upload/replace documents
- Fill/edit forms
- Delete package
- Submit when ready

**EAO Can:**
- Not visible to EAO yet

**Duration:** Variable - until user submits

**Business Context:** This is the working state where the proponent prepares their submission.

#### 2. SUBMITTED

**Meaning:** Package sent to EAO, awaiting initial review.

**User Can:**
- View package (read-only)
- View submission confirmation
- Track status
- Cannot edit (locked)

**EAO Can:**
- View package
- Assign reviewers
- Begin review process
- Change status

**Duration:** Typically 1-5 business days

**Business Context:** Package is in EAO's queue, waiting for review assignment.

#### 3. UNDER_REVIEW

**Meaning:** EAO staff actively reviewing the submission.

**Sub-Statuses:**
- **Under Consultation Check**: Verifying consultation requirements
- **Passed Consultation Check**: Consultation verified, moving to technical review
- **Failed Consultation Check**: Consultation inadequate, revision required
- **Under Technical Review**: Subject matter experts reviewing content
- **Awaiting Manager Approval**: Final approval pending

**User Can:**
- View package
- View review progress
- Respond to questions from EAO
- Cannot edit package

**EAO Can:**
- Review items
- Add review notes
- Request additional information
- Approve, reject, or request revision

**Duration:** Variable - typically 30-90 days depending on complexity

**Business Context:** This is the main review period where EAO assesses the submission.

#### 4. APPROVED

**Meaning:** Package meets all requirements and is accepted.

**User Can:**
- View approved package
- Download approval letter
- Reference in future submissions

**EAO Can:**
- View package
- Generate compliance reports

**Duration:** Permanent end state

**Business Context:** Proponent has met their obligation for this submission. Package serves as record of compliance.

#### 5. REVISION_REQUIRED

**Meaning:** Package needs changes before it can be approved.

**User Can:**
- View original package (read-only)
- View EAO's revision requests
- Create new package version
- Address identified issues
- Resubmit

**EAO Can:**
- View package
- Track resubmission
- Review new version when submitted

**Duration:** Until proponent resubmits

**Business Context:** EAO has identified deficiencies that must be corrected. This is not a rejection - the proponent can address the issues and resubmit.

**Common Reasons for Revision:**
- Missing information
- Inadequate detail in plans
- Insufficient monitoring programs
- Unclear descriptions
- Outdated data
- Non-compliance with conditions

#### 6. REJECTED

**Meaning:** Package does not meet requirements and is not accepted.

**User Can:**
- View rejected package
- View rejection reasons
- May need to create entirely new submission

**EAO Can:**
- View package
- Document rejection rationale

**Duration:** Permanent end state

**Business Context:** Rejection is rare and typically occurs when fundamental requirements are not met or when there are serious compliance concerns. Different from revision required - rejection means the submission is not salvageable with minor changes.

#### 7. RESUBMITTED

**Meaning:** New version created in response to revision request.

**User Can:**
- Edit new version
- Reference original submission
- Address EAO feedback
- Submit when ready

**EAO Can:**
- View both original and new version
- Compare changes
- Review resubmission

**Duration:** Until submitted, then returns to UNDER_REVIEW

**Business Context:** This status indicates the proponent is actively addressing EAO's concerns.

---

## Version Control and Resubmission

### Why Version Control?

**Business Needs:**
- Track changes over time
- Maintain audit trail
- Compare versions
- Understand evolution of submissions
- Support compliance verification

### Version Numbering

**Format:** Major.Minor (e.g., 1.0, 1.1, 2.0)

**Major Versions:**
- Created when package is resubmitted to EAO
- Indicates significant changes
- Triggered by revision requests
- Example: 1.0 → 2.0

**Minor Versions:**
- Created when documents are replaced within a version
- Indicates small updates or corrections
- Does not require resubmission
- Example: 1.0 → 1.1

### Resubmission Process

**Trigger:** EAO requests revisions

**Step 1: Receive Revision Request**
- EAO changes package status to "Revision Required"
- EAO provides specific feedback on what needs to change
- User receives email notification
- User reviews EAO's comments

**Step 2: Create New Version**
- User clicks "Create Resubmission"
- System creates new package version
- All content from previous version is copied
- New version number assigned (e.g., v1 → v2)
- Status set to "Resubmitted"

**Step 3: Make Changes**
- User edits items that need revision
- Can replace documents
- Can update form data
- Can add new information
- Previous version remains unchanged for reference

**Step 4: Document Changes**
- User adds notes explaining what was changed
- References EAO's feedback
- Highlights key updates
- Provides rationale for changes

**Step 5: Submit New Version**
- User submits when changes are complete
- System validates completeness
- New version sent to EAO
- EAO reviews changes

**Step 6: EAO Reviews Resubmission**
- EAO compares new version to original
- Verifies requested changes were made
- Assesses adequacy of revisions
- Makes final decision (approve, reject, or request further revision)

### Version History

**What's Tracked:**
- All package versions
- All document versions within each package
- All form data changes
- Who made each change
- When changes were made
- Why changes were made (if documented)

**Accessing History:**
- Users can view all versions of their packages
- Can download previous versions
- Can see timeline of changes
- Can compare versions side-by-side

**Business Value:**
- Demonstrates responsiveness to EAO feedback
- Shows evolution of compliance approach
- Supports learning and improvement
- Provides evidence for audits

---

## Document Management

### Document Upload

**Process:**
1. Navigate to item
2. Click "Upload Document"
3. Select file
4. Add description (optional but recommended)
5. Confirm upload

**System Actions:**
- Validates file type and size
- Scans for viruses
- Stores in secure document repository
- Creates database record
- Links to item
- Generates version number

### Document Replacement

**When to Replace:**
- Correcting errors in document
- Updating with newer information
- Improving quality or clarity
- Adding missing content

**Process:**
1. Navigate to item with existing document
2. Click "Replace Document"
3. Upload new file
4. System increments version number
5. Previous version archived but accessible

**Business Rule:**
- Can only replace documents before package is submitted
- After submission, must create new package version

### Document Organization

**Best Practices:**

**File Naming:**
- Use descriptive names
- Include version numbers
- Include dates if relevant
- Use consistent format
- Example: "2024_Wildlife_Monitoring_Plan_v1.0.pdf"

**Document Descriptions:**
- Briefly explain document content
- Note any special considerations
- Reference related documents
- Example: "Detailed wildlife monitoring plan for 2024, including survey methods and reporting schedule"

**File Formats:**
- Use PDF for final documents (ensures formatting preserved)
- Use native formats (Word, Excel) for working documents
- Compress large files
- Combine related files into single PDF when appropriate

### Document Security

**Access Control:**
- Only authorized users can view documents
- Staff can see all submitted documents
- Proponents can only see their own documents
- Document access logged

**Data Protection:**
- Documents encrypted in storage
- Secure transmission (HTTPS)
- Regular backups
- Disaster recovery procedures

---

## Form Submissions

### When to Use Forms

**Appropriate for:**
- Contact information
- Numerical data (measurements, quantities)
- Dates and timelines
- Selections from predefined lists
- Yes/no questions
- Short text responses

**Not Appropriate for:**
- Long narrative descriptions
- Complex technical analysis
- Maps and diagrams
- Photos and images
- Large datasets

### Form Features

**Data Validation:**
- Required fields enforced
- Format validation (email, phone, dates)
- Range checking (numbers within acceptable limits)
- Logic validation (end date after start date)
- Real-time feedback as user types

**User Experience:**
- Clear field labels
- Help text for complex fields
- Dropdown lists for predefined options
- Date pickers for easy date selection
- Character counters for text fields
- Save draft functionality

**Data Quality:**
- Consistent formatting
- Reduced errors
- Complete information
- Structured for analysis

### Form Editing

**Before Submission:**
- Can edit anytime
- Changes saved automatically or manually
- Can save partial completion
- Can return later to finish

**After Submission:**
- Forms locked (read-only)
- To change, must create new package version
- All changes tracked in version history

---

## Business Rules and Validations

### Package Creation Rules

1. **User must have permission** to create packages for the project
2. **Project must be active** and assigned to user's account
3. **Package name must be unique** within the project
4. **Reporting period must be logical** (end date after start date)
5. **Cannot create duplicate packages** for the same period and type

### Submission Rules

1. **All mandatory items must be complete** before submission
2. **At least one submission per mandatory item** (document or form)
3. **Package metadata must be complete** (contacts, dates, etc.)
4. **User must have submission permission**
5. **Cannot submit package that's already submitted** (must create new version)

### Document Rules

1. **File size limits enforced** (typically 100 MB per file)
2. **Only approved file types accepted** (PDF, Word, Excel, images, etc.)
3. **Files must pass virus scanning**
4. **File names cannot contain special characters** that cause system issues
5. **Cannot delete documents after submission** (can only add new versions)

### Form Rules

1. **Required fields must be completed**
2. **Data must match expected format** (email, phone, date, number)
3. **Numerical values must be within acceptable ranges**
4. **Date logic must be valid** (end dates after start dates)
5. **Cannot leave form partially complete** when submitting package

### Version Control Rules

1. **Cannot edit submitted packages** - must create new version
2. **Version numbers automatically assigned** - cannot be manually set
3. **Previous versions cannot be deleted** - maintained for audit trail
4. **Resubmissions must reference original version**
5. **Version history is immutable** - cannot alter past records

### Status Transition Rules

1. **NEW → SUBMITTED**: User action, requires validation pass
2. **SUBMITTED → UNDER_REVIEW**: EAO staff action
3. **UNDER_REVIEW → APPROVED**: EAO staff action after successful review
4. **UNDER_REVIEW → REVISION_REQUIRED**: EAO staff action when changes needed
5. **UNDER_REVIEW → REJECTED**: EAO staff action for fundamental issues
6. **REVISION_REQUIRED → RESUBMITTED**: User creates new version
7. **RESUBMITTED → SUBMITTED**: User submits new version
8. **Cannot reverse status** once moved forward (except via resubmission)

---

## Common Business Scenarios

### Scenario 1: First-Time Management Plan Submission

**Context:** Mining company submitting their first annual management plan.

**Process:**
1. Environmental manager creates new Management Plan package
2. Enters metadata (2024 reporting period, contact info)
3. System generates 9 required items
4. Team works on items over 2 weeks:
   - Manager completes project overview
   - Biologist completes wildlife monitoring section
   - Engineer completes water management section
   - Consultant completes air quality section
5. Manager reviews all items for completeness
6. Manager submits package to EAO
7. EAO conducts consultation check (passes)
8. EAO conducts technical review
9. EAO requests revision on monitoring frequency
10. Manager creates new version, increases monitoring frequency
11. Manager resubmits
12. EAO approves revised plan

**Outcome:** Approved management plan, lessons learned for next year.

### Scenario 2: Quarterly IEM Report

**Context:** IEM submitting Q1 2024 monitoring report.

**Process:**
1. IEM creates new IEM Report package
2. Enters Q1 dates (Jan 1 - Mar 31, 2024)
3. Completes monitoring activities item (form + document)
4. Uploads site visit reports
5. Completes compliance assessment
6. Notes one minor non-compliance issue
7. Provides recommendations
8. Submits to EAO
9. EAO reviews quickly (routine submission)
10. EAO approves within 2 weeks

**Outcome:** Timely approval, minor issue flagged for follow-up.

### Scenario 3: Consultation Record with Multiple Revisions

**Context:** Proponent submitting consultation record before major project decision.

**Process:**
1. Consultation coordinator creates Consultation Record package
2. Uploads meeting notes, correspondence, agreements
3. Submits to EAO
4. EAO reviews, finds consultation inadequate
5. EAO requests revision: need more detail on how concerns were addressed
6. Coordinator creates new version
7. Adds detailed response table showing each concern and response
8. Resubmits
9. EAO reviews, still finds gaps
10. EAO requests second revision: need evidence of follow-up
11. Coordinator creates third version
12. Adds follow-up meeting notes and commitment tracking
13. Resubmits
14. EAO approves

**Outcome:** Approved after multiple iterations, demonstrates importance of thorough consultation documentation.

---

*This document covers package and submission workflows in EPIC.submit. For information on the review process, see the Review and Approval Process documentation.*
