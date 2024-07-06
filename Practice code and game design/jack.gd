extends CharacterBody2D
# These are values that affect how fast the player character moves.
# const stays the same no matter what perfect for capping speed
var SPEED = 300.0
const JUMP_VELOCITY = -700.0

#brings the payers arm into the character
@export var player_arms : PackedScene
# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")
func _ready():
	player_arms.instantiate()

func _physics_process(delta):
	# Add the gravity. This is generated code
	if not is_on_floor():
		velocity.y += gravity * delta

	# Handle Jump. Same here
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions. and below but that is the end of the generated code.
	var direction = Input.get_axis("move_left", "move_right")
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
	move_and_slide()
	#This is for the character to sprint or run faster
	if Input.is_action_pressed("sprint") and Input.is_action_pressed("move_left"):
		SPEED = 550
	elif Input.is_action_pressed("sprint") and Input.is_action_pressed("move_right"):
		SPEED = 550
	else:
		SPEED = 300
	
