extends Area2D

@export var victory_screen : PackedScene
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
	
func _on_body_shape_entered(body_rid, body, body_shape_index, local_shape_index):
	print ("Winner") # You win
	victory_screen.instantiate()
