extends RigidBody2D

var health = 15

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass




func _on_area_2d_area_entered(area):
	health -= 4
	print(health)
	if health <= 0:
		queue_free()
