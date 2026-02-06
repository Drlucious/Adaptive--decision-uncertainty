# Adaptive Decision-Making from Internal Numerical Error

## Overview
This repository contains a PsychoPy-based experimental paradigm investigating how internally generated numerical estimation error and subjective confidence influence 
risk-based decision-making in the absence of trial-by-trial external feedback.
Participants estimate numerical quantities from visual or auditory stimuli, report their confidence, and chosen between a safe or risky reward option. 
Only cumulative feedback is presented at the end of the experiment.

## Experimental Design
- Between subjects: Sensory modality (Visual vs Auditory)
- Within-Subjects: Task difficulty (Easy vs Hard)
- Dependent variables:
   - Numerical estimation error
   - Confidence rating
   - Risk choice (safe vs risky)
   - Confidence & Decision RT
   - Cumulative Points

## Repository Structure
- experiment/ --> PsychoPy Task Files
- conditions/ --> Trial Condition Spreadsheets
- stimuli/ --> Images and Sound Files
- docs/ --> Methods and deployment documentation

## Running Online 
See 'docs/deployment.md` for Pavlovia instructions.

## Data Output
CSV files include:
- estimate_raw
- estimate_value
- true_value
- threshold
- confidence
- confidence_rt
- choice_text
- earned_points
- abs_error
- total_points

## Author
Gift Ayo
Researcher










