//Attach this code to the cube.
//Be sure you also add a rigidbody to the cube and
//set the goal of this script, in the inspector to
//be the fp controller

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//this script doesn't require a rigidbody
//but this is here to make sure you
//add one to the cube along with this code
[RequireComponent(typeof(Rigidbody))]

public class FollowPlayer : MonoBehaviour {

	public float speed = 2.0f;
	public float accuracy = 20.0f;

	//Drag and drop your FPSController from the Hierarchy
	//onto this goal in the inspector for the cube to follow.
	public Transform goal;

    Animator animator = null;

	// Use this for initialization
	void Start () {
        animator = this.GetComponent<Animator>();
	}

    // Update is called once per frame
    void Update()
    {

        //Vector3 lookAtGoal = new Vector3(goal.transform.position.x,
        //this.transform.position.y,
        //goal.transform.position.z);

        //Vector3 direction = lookAtGoal - this.transform.position;

        //this.transform.rotation = Quaternion.Slerp(this.transform.rotation,
        //Quaternion.LookRotation(direction),
        //Time.deltaTime * speed);

        this.transform.LookAt(goal.position);
        Vector3 direction = goal.position - this.transform.position;

        if (direction.magnitude > accuracy)
        {
            //this.transform.Translate(0, 0, speed * Time.deltaTime);
            this.transform.Translate(direction.normalized * speed * Time.deltaTime, Space.World);
            if (animator != null) animator.SetBool("isMoving", true);
        }
        else
        {
            if (animator != null) animator.SetBool("isMoving", false);
        }
    }
}
