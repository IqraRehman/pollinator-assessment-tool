# Overview

This is a Streamlit web application that provides an interactive assessment tool for evaluating how cleaning practices affect pollinator health. The app guides users through a questionnaire about their cleaning habits, calculates an eco-friendliness score, and provides personalized recommendations to make their practices more pollinator-friendly. The application features an animated mascot guide (Buzzy the bee), generates shareable results cards, and creates downloadable PDF guides with natural cleaning recipes.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: Streamlit for the web application interface
- **Multi-page Structure**: Uses Streamlit's page navigation system with separate files for questionnaire and recommendations
- **Interactive Elements**: Custom CSS animations for buttons, progress bars, and hover effects
- **Responsive Design**: Column-based layouts with mobile-friendly components

## Application Structure
- **Main Entry Point**: `main.py` serves as the landing page with introduction and navigation
- **Page System**: Modular page structure with questionnaire (`01_questionnaire.py`) and recommendations (`02_recommendations.py`)
- **Data Layer**: Centralized question bank and recommendation database in `data/` directory
- **Utility Layer**: Reusable components for scoring, PDF generation, progress tracking, and mascot interactions

## Core Components
- **Assessment Engine**: Score calculation system that evaluates user responses against pollinator-friendly criteria
- **Recommendation System**: Tiered advice system (low/medium/high) based on calculated scores
- **Progress Tracking**: Visual progress indicators with animated elements and mascot feedback
- **Content Generation**: PDF generation for personalized cleaning guides and recipe collections

## User Experience Features
- **Animated Mascot**: Buzzy the bee provides contextual tips and encouragement throughout the assessment
- **Visual Feedback**: Custom progress bars with growth-themed animations and emoji indicators
- **Educational Content**: Tooltips and explanations connecting cleaning practices to pollinator impact
- **Shareable Results**: QR code generation and downloadable content for sharing achievements

## Styling and Theming
- **Custom CSS**: Animations for user interactions, hover effects, and visual transitions
- **Color Scheme**: Eco-friendly green palette (#4CAF50, #8BC34A) with nature-inspired design elements
- **Typography**: Clear, accessible fonts with proper hierarchy and spacing

# External Dependencies

## Core Framework
- **Streamlit**: Web application framework for the entire user interface
- **PIL (Pillow)**: Image processing for loading external images and generating visual content

## PDF and Document Generation
- **ReportLab**: PDF generation library for creating downloadable guides and recipe collections
- **QRCode**: QR code generation for shareable content and external links

## External Services
- **Unsplash API**: Image loading from external URLs for visual content
- **HTTP Requests**: Image fetching and content loading via the `requests` library

## Potential Future Integrations
- **Database Storage**: User response persistence and analytics tracking
- **Email Services**: Automated follow-up recommendations and progress tracking
- **Social Sharing APIs**: Direct sharing to social media platforms
- **Analytics Services**: User behavior tracking and assessment completion metrics