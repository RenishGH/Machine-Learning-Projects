import joblib
import numpy as np

# --- Configuration ---
# List the EXACT features used for X, in the correct order
FEATURES_TO_INPUT = [
    'Daily Time Spent on Site', # float
    'Age',                      # int
    'Area Income',              # float
    'Daily Internet Usage',     # float
    'Male'                      # int (0 or 1)
]
MODEL_FILE = 'logistic_model_no_scaling.joblib' # Use the correct filename

# --- Load Saved Model ---
print("Loading model...")
try:
    model = joblib.load(MODEL_FILE)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model file '{MODEL_FILE}' not found.")
    print("Make sure it's in the same directory as this script.")
    exit()
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# --- Get User Input ---
print("\n--- Please enter the user details ---")
user_input_values = []
for feature in FEATURES_TO_INPUT:
    while True: # Loop for basic validation
        value_str = input(f"Enter {feature}: ")
        try:
            if feature == 'Age':
                value = int(value_str)
            elif feature == 'Male':
                 value = int(value_str)
                 if value not in [0, 1]:
                     print("Input for 'Male' must be 0 or 1.")
                     continue # Ask again
            else: # Assume float for the others
                 value = float(value_str)

            user_input_values.append(value)
            break # Exit validation loop if input is okay

        except ValueError:
            print(f"Invalid input type for {feature}. Please try again.")

# --- Prepare Input for Model ---
# Convert list to a 2D NumPy array (model expects 2D input: [samples, features])
# The order must match FEATURES_TO_INPUT
try:
    input_array = np.array([user_input_values])
    print(f"\nInput values prepared: {input_array}")
except Exception as e:
    print(f"Error creating input array: {e}")
    exit()

# --- Make Prediction ---
# NO SCALING step needed here
print("Making prediction...")
try:
    prediction = model.predict(input_array)
    probability = model.predict_proba(input_array)
    click_probability = probability[0][1] # Probability for class '1'
except Exception as e:
    print(f"Error during prediction: {e}")
    exit()

# --- Display Result ---
print("\n--- Prediction Result ---")
if prediction[0] == 1:
    print("✅ Prediction: The user is LIKELY to click the ad (Class 1).")
else:
    print("❌ Prediction: The user is UNLIKELY to click the ad (Class 0).")

print(f"(Model's estimated probability of clicking: {click_probability:.2%})")

# --- END OF CODE TO PASTE ---