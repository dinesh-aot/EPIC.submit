# EPIC.submit Business Documentation

## Welcome

This documentation provides a comprehensive business-focused overview of the EPIC.submit system, covering all aspects of how the system works, why it exists, and how it delivers value to users. The documentation is written for business stakeholders, project managers, and anyone who needs to understand the system without deep technical knowledge.

---

## Documentation Structure

### 📚 [Business Overview](./BUSINESS_OVERVIEW.md)
**Start here for a high-level understanding of the system**

This document covers:
- What EPIC.submit is and why it exists
- Key stakeholders (proponents and EAO staff)
- Core business capabilities
- System architecture overview (non-technical)
- Business value and benefits
- Success metrics

**Best for**: New team members, executives, business analysts, project sponsors

---

### 👥 [User Management and Roles](./USER_MANAGEMENT_AND_ROLES.md)
**Understanding users, roles, and permissions**

This document covers:
- User types (proponent users vs. staff users)
- Complete user onboarding process
- Detailed breakdown of all proponent roles and permissions
- Staff roles and their capabilities
- Account structure and management
- User lifecycle management
- Security and access control principles

**Best for**: Account administrators, user managers, security officers, training coordinators

---

### 📦 [Package and Submission Workflow](./PACKAGE_AND_SUBMISSION_WORKFLOW.md)
**How submissions are created, managed, and submitted**

This document covers:
- Package types (Management Plans, IEM Reports, Consultation Records)
- Package structure and components
- Complete package creation workflow
- Submission process and validation
- Package status lifecycle
- Version control and resubmission process
- Document and form management
- Business rules and validations

**Best for**: Proponent users, submission coordinators, process designers, trainers

---

### ✅ [Review and Approval Process](./REVIEW_AND_APPROVAL_PROCESS.md)
**How EAO staff review and approve submissions**

This document covers:
- Three-stage review process (Consultation Check, Technical Review, Manager Approval)
- Detailed review procedures for each stage
- Review tools and features
- Communication during review
- Decision types (Approval, Revision Required, Rejection)
- Update requests
- Review timelines and service level agreements

**Best for**: EAO staff, reviewers, managers, quality assurance, process improvement teams

---

### 🔗 [Integration and System Architecture](./INTEGRATION_AND_SYSTEM_ARCHITECTURE.md)
**How the system connects with other systems and operates**

This document covers:
- System components (frontend, backend, database)
- External system integrations (EPIC.Track, EPIC.Document, EPIC.Conditions, EPIC.Cron)
- Authentication and identity management (Keycloak, IDIR, BCeID)
- Data flow and synchronization
- Email and notification system
- Document storage and management
- Activity logging and audit trail
- Security architecture
- Business continuity and disaster recovery

**Best for**: System administrators, integration specialists, security teams, operations staff

---

## Quick Reference

### Common Questions

**Q: How do I invite a new user?**
→ See [User Management and Roles](./USER_MANAGEMENT_AND_ROLES.md#user-onboarding-process)

**Q: What are the different package types?**
→ See [Package and Submission Workflow](./PACKAGE_AND_SUBMISSION_WORKFLOW.md#package-types)

**Q: How long does a review take?**
→ See [Review and Approval Process](./REVIEW_AND_APPROVAL_PROCESS.md#review-timelines-and-slas)

**Q: What happens if I need to revise my submission?**
→ See [Package and Submission Workflow](./PACKAGE_AND_SUBMISSION_WORKFLOW.md#version-control-and-resubmission)

**Q: How does the system integrate with EPIC.Track?**
→ See [Integration and System Architecture](./INTEGRATION_AND_SYSTEM_ARCHITECTURE.md#epictrack-integration)

**Q: What are the different user roles?**
→ See [User Management and Roles](./USER_MANAGEMENT_AND_ROLES.md#proponent-roles-and-permissions)

**Q: How does the consultation check work?**
→ See [Review and Approval Process](./REVIEW_AND_APPROVAL_PROCESS.md#consultation-check-process)

**Q: Where are documents stored?**
→ See [Integration and System Architecture](./INTEGRATION_AND_SYSTEM_ARCHITECTURE.md#document-storage-and-management)

---

## Document Conventions

### Icons and Symbols

- ✅ **Allowed/Permitted**: User can perform this action
- ❌ **Not Allowed/Restricted**: User cannot perform this action
- 📋 **Process/Workflow**: Step-by-step procedure
- ⚠️ **Important Note**: Pay special attention
- 💡 **Best Practice**: Recommended approach
- 🔍 **Example**: Illustrative scenario

### Status Indicators

Throughout the documentation, you'll see various status terms:

**Package Statuses**:
- **NEW**: Just created, not submitted
- **SUBMITTED**: Sent to EAO
- **UNDER_REVIEW**: Being evaluated
- **APPROVED**: Accepted
- **REVISION_REQUIRED**: Changes needed
- **REJECTED**: Not accepted

**Item Statuses**:
- **NEW**: Not started
- **IN_PROGRESS**: Being worked on
- **SUBMITTED**: Completed
- **APPROVED**: Accepted
- **REVISION_REQUIRED**: Needs changes

**User Statuses**:
- **ACTIVE**: Can access system
- **INACTIVE**: No access
- **PENDING**: Invitation sent but not accepted

---

## How to Use This Documentation

### For New Users

1. Start with [Business Overview](./BUSINESS_OVERVIEW.md) to understand the big picture
2. Read [User Management and Roles](./USER_MANAGEMENT_AND_ROLES.md) to understand your role
3. Review [Package and Submission Workflow](./PACKAGE_AND_SUBMISSION_WORKFLOW.md) to learn how to create submissions
4. Reference other documents as needed for specific topics

### For Administrators

1. Review [User Management and Roles](./USER_MANAGEMENT_AND_ROLES.md) for user administration
2. Understand [Integration and System Architecture](./INTEGRATION_AND_SYSTEM_ARCHITECTURE.md) for system operations
3. Reference [Business Overview](./BUSINESS_OVERVIEW.md) for strategic context
4. Use workflow documents to train users

### For EAO Staff

1. Start with [Business Overview](./BUSINESS_OVERVIEW.md) for context
2. Focus on [Review and Approval Process](./REVIEW_AND_APPROVAL_PROCESS.md) for your primary work
3. Reference [Package and Submission Workflow](./PACKAGE_AND_SUBMISSION_WORKFLOW.md) to understand what proponents see
4. Review [User Management and Roles](./USER_MANAGEMENT_AND_ROLES.md) for permission details

### For Business Analysts and Process Designers

1. Read all documents to understand the complete system
2. Pay special attention to business rules and validations
3. Review business scenarios in each document
4. Use as reference for process improvement initiatives

---

## Documentation Maintenance

### Version History

- **Version 1.0** (January 2026): Initial comprehensive business documentation created

### Updates and Corrections

This documentation reflects the current state of the EPIC.submit system. As the system evolves, documentation will be updated to reflect changes.

If you find errors or areas that need clarification:
1. Contact the EPIC.submit product team
2. Provide specific document and section references
3. Suggest improvements or corrections

---

## Additional Resources

### Related Documentation

- **EPIC.submit User Guide**: Step-by-step instructions for common tasks (separate document)
- **EPIC.submit Technical Documentation**: Detailed technical implementation guide (for developers)
- **EPIC.submit API Documentation**: API reference and integration guide (for developers)
- **EPIC.Track Documentation**: Information about the project management system
- **EPIC.Document Documentation**: Document storage system details

### Training and Support

- **User Training**: Contact EAO training coordinator for scheduled sessions
- **Help Desk**: Submit support tickets for technical issues
- **Product Team**: Contact for feature requests and feedback
- **Documentation Feedback**: Send suggestions for documentation improvements

---

## Glossary of Terms

**Account**: Organizational container for a proponent's users, projects, and submissions

**Certificate Holder**: Organization that holds an environmental assessment certificate

**Consultation Record (CR)**: Documentation of Indigenous consultation activities

**EAO**: Environmental Assessment Office of British Columbia

**EPIC**: Environmental Assessment Process Information and Collaboration (suite of systems)

**IEM**: Independent Environmental Monitor

**Item**: Individual section or requirement within a package

**Keycloak**: Identity and access management system

**Management Plan (MP)**: Annual plan describing environmental management approach

**Package**: Complete submission container with all required documents and forms

**Proponent**: Organization that holds an environmental certificate or exemption

**Resubmission**: New version of a package created in response to revision request

**Submission**: Actual content (document or form) provided for an item

**Version**: Numbered iteration of a package or submission

---

## Contact Information

### EPIC.submit Product Team
- **Email**: epic.submit@gov.bc.ca
- **Phone**: 1-XXX-XXX-XXXX

### Technical Support
- **Help Desk**: support.epic@gov.bc.ca
- **Hours**: Monday-Friday, 8:30 AM - 4:30 PM Pacific Time

### Training
- **Training Coordinator**: training.epic@gov.bc.ca
- **Schedule**: Quarterly training sessions, on-demand for new users

---

## Document Information

**Created**: January 2026  
**Last Updated**: January 2026  
**Version**: 1.0  
**Maintained By**: EPIC.submit Product Team  
**Classification**: Public

---

*This documentation is designed to be comprehensive yet accessible. Whether you're a new user learning the system or an experienced administrator seeking specific information, you'll find detailed explanations of all business processes and logic in EPIC.submit.*
