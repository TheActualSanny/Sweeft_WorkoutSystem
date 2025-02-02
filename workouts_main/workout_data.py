'''
    There will be a single constant variable here which will store the data of the 
    20 predefined excercises. The tuple will be used inside the first migration to
    instantiate the  model with initial data.
'''

DEFINED_WORKOUTS = ({'workout_name' : 'Bicep Curls', 'workout_instruction' : '''Stand tall, hold a dumbbell in each hand with palms facing forward. Curl the weights toward your shoulders, 
                     keeping elbows close to your sides. Slowly lower back to start.''', 'workout_description' : 'Focuses on building bicep strength and size by isolating the upper arm muscles.', 'muscle_group' : 'Biceps'},
                    {'workout_name' : 'Tricep Dips', 'workout_instruction' : '''Sit on a bench, hands gripping the edge beside your hips. Extend your legs out, 
                     lower your body by bending elbows, then push back up.''', 'workout_description' : 'A great bodyweight exercise to target the triceps by lowering and raising the body.', 'muscle_group' : 'Triceps'},
                    {'workout_name' : 'Leg Extensions', 'workout_instruction' : '''Sit on a leg extension machine, place your feet under the pad. 
                     Extend your legs until they’re straight, then lower slowly.''', 'workout_description' : 'Isolates the quadriceps to improve leg strength.', 'muscle_group' : 'Quads'},
                    {'workout_name' : 'Hamstring Curls', 'workout_instruction' : '''Lie face down on a leg curl machine, position your legs under the pad. 
                     Curl your legs upward, squeezing the hamstrings, then lower slowly.''', 'workout_description' : 'Focuses on the hamstrings by bending the knees against resistance.', 'muscle_group' : 'Hamstrings'},
                    {'workout_name' : 'Chest Flyes', 'workout_instruction' : '''Lie on a bench holding dumbbells in both hands. With a slight bend in your elbows, 
                     slowly open your arms wide, then bring them back together.''', 'workout_description' : 'Stretches and strengthens the chest muscles by isolating them with a flying motion.', 'muscle_group' : 'Chest'},
                    {'workout_name' : 'Lat Pulldowns', 'workout_instruction' : '''Sit at a lat pulldown machine, grip the bar wider than shoulder-width. 
                     Pull the bar down to your chest, squeezing your lats, then release.''', 'workout_description' : 'Targets the latissimus dorsi muscles in the back, improving width.', 'muscle_group' : 'Lats'},
                    {'workout_name' : 'Shrugs', 'workout_instruction' : '''Stand tall, holding a dumbbell or barbell in each hand. Shrug your shoulders upward, 
                     hold for a moment, then lower back down.''', 'workout_description' : 'Builds the trapezius muscles to strengthen the upper back and neck.', 'muscle_group' : 'Upper Back'},
                    {'workout_name' : 'Seated Rows', 'workout_instruction' : 'Sit at a row machine with feet secured. Pull the handle toward your torso, squeezing your shoulder blades together, then slowly release.', 
                     'workout_description' : 'Targets the middle of the back, focusing on the rhomboids and traps.', 'muscle_group' : 'Middle Back'},
                    {'workout_name' : 'Lateral Raises', 'workout_instruction' : '''Stand holding dumbbells at your sides. Lift the weights outward to shoulder height, keeping a slight bend in your elbows, then lower slowly.''', 
                     'workout_description' : 'Isolates the lateral deltoid for wider shoulders.', 'muscle_group' : 'Lateral Delts'},
                    {'workout_name' : 'Front Raises', 'workout_instruction' : 'Hold dumbbells in front of your thighs. Lift the dumbbells straight in front of you until arms are parallel to the ground, then lower.', 
                     'workout_description' : 'Targets the front deltoids for shoulder development.', 'muscle_group' : 'Front Delts'},
                    {'workout_name' : 'Concentration Curls', 'workout_instruction' : 'Sit on a bench, lean forward and place one arm on your thigh. Curl a dumbbell toward your shoulder, squeezing at the top, then lower slowly.', 
                     'workout_description' : 'Isolates the biceps for a more intense contraction.', 'muscle_group' : 'Biceps'},
                    {'workout_name' : 'Overhead Tricep Extensions', 'workout_instruction' : 'Hold a dumbbell with both hands above your head. Lower the weight behind your head by bending your elbows, then extend your arms back up.', 
                     'workout_description' : 'Focuses on the long head of the triceps, enhancing arm strength.', 'muscle_group' : 'Triceps'},
                    {'workout_name' : 'Glute Bridges', 'workout_instruction' : 'Lie on your back with knees bent and feet flat. Lift your hips to create a straight line from shoulders to knees, squeezing your glutes at the top, then lower.', 
                     'workout_description' : 'Strengthens and tones the glutes, targeting the posterior chain.', 'muscle_group' : 'Glutes'},
                    {'workout_name' : 'Leg Press', 'workout_instruction' : 'Sit on the leg press machine, place feet shoulder-width apart on the platform. Push the platform upward, extend your legs, then lower slowly.', 
                     'workout_description' : 'Focuses on the quads with controlled movement and heavy weight.', 'muscle_group' : 'Quads'},
                    {'workout_name' : 'Cable Kickbacks', 'workout_instruction' : 'Attach an ankle strap to a low cable machine. Secure it around your ankle, and extend your leg backward, squeezing your glute, then return slowly.', 
                     'workout_description' : 'Isolates the glutes by extending the leg behind the body.', 'muscle_group' : 'Glutes'},
                    {'workout_name' : 'Reverse Flyes', 'workout_instruction' : 'Stand with a slight bend in your knees, hold dumbbells in front of you. Open your arms wide to the sides, squeezing the rear delts, then return.', 
                     'workout_description' : 'Targets the rear deltoids, helping with shoulder stability and posture.', 'muscle_group' : 'Read Delts'},
                    {'workout_name' : 'Ab Rollouts', 'workout_instruction' : 'Kneel on the floor holding an ab wheel. Roll the wheel forward, extending your body, then pull back to the starting position.', 
                     'workout_description' : 'Engages the entire core, particularly the abs and lower back.', 'muscle_group' : 'Abcs'},
                    {'workout_name' : 'Side Planks', 'workout_instruction' : 'Lie on your side, supporting your body with your forearm. Keep your body in a straight line, and hold the position for as long as possible.', 
                     'workout_description' : 'Targets the obliques for a stronger core and improved stability.', 'muscle_group' : 'Obliques'},
                    {'workout_name' : 'Calf Raises', 'workout_instruction' : 'Stand with feet shoulder-width apart, then rise onto the balls of your feet, lifting your heels as high as possible. Lower back down slowly.', 
                     'workout_description' : 'Strengthens the calf muscles (gastrocnemius and soleus).', 'muscle_group' : 'Calves'},
                    {'workout_name' : 'Cable Face Pulls', 'workout_instruction' : 'Set the rope attachment on a high pulley. Grab the rope with both hands, pull it toward your face while keeping elbows high, and squeeze your shoulder blades together.', 
                     'workout_description' : 'Works the rear delts and upper back, improving posture and shoulder health.', 'muscle_group' : 'Read Delts'})
                    


    
