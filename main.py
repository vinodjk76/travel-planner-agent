from src.agent import TravelPlannerCrew
def main():
    # ... (Keep your argparse code setup from before) ...
    
    # Pack parameters to inject directly into the matching YAML brackets {placeholder}
    inputs = {
        'destination': args.destination,
        'days': args.days,
        'budget': args.budget,
        'interests': args.interests
    }
    
    print(f"✈️ Planning your trip to {args.destination}...")
    
    # Initialize and execute the crew class wrapper
    travel_crew = TravelPlannerCrew()
    result = travel_crew.crew().kickoff(inputs=inputs)
    
    print("\n🗺️ YOUR PERSONALIZED ITINERARY:")
    print("=================================")
    print(result.raw)
