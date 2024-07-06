extends StaticBody2D

#this is a cooldown for when to fire the gun again
var guncooldown = true
#Calls other scenes and code from other scripts to add function
@export var bullet : PackedScene
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	look_at(get_global_mouse_position())
	if Input.is_action_just_pressed("action"):
		var r = randf_range(-.20, .20)#This is to make the gun not 100% accurate
		rotate(r)
		#Make sure to create the shoot function before you uncomment this
		shoot()
	
	
#This is the function that allows the player to shoot their weapeon
func shoot():
	if not guncooldown:
		return
	guncooldown = false
	$guncooldown.start()
	#edit these to fit in
	var b = bullet.instantiate()
	get_tree().root.add_child(b)
	b.transform = $muzzle.global_transform


func _on_guncooldown_timeout():
	guncooldown = true # Replace with function body.
