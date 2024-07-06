extends Area2D
#This is how fast the bullet goes
const speed = 1000
#This is to tell the bullet it hits something
signal hit
#This is how much damage that the weapeon did
var dam = randf_range(10, 16)
#This is for timer

# Called when the node enters the scene tree for the first time.
func _ready():
	pass
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	position += transform.x * speed * delta
	
	
#This removes bullets when they go off screen
func _on_visible_on_screen_notifier_2d_screen_exited():
	queue_free()


func _on_length_timeout():
	queue_free()

#This mades the bullets disapear when they hit a surface or enemy
func _on_body_shape_entered(body_rid, body, body_shape_index, local_shape_index):
	if body.is_in_group("jack"):
		pass
	else:
		queue_free()
