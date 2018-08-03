using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WaypointFollow : MonoBehaviour
{
    public GameObject[] waypoints;
    int currWP = 0;

    float speed = 3.0f;
    float accuracy = 1.0f;
    float rotSpeed = 0.6f;


    // Use this for initialization
    void Start()
    {
        waypoints = GameObject.FindGameObjectsWithTag("waypoint");
    }

    // Update is called once per frame
    void LateUpdate()
    {
        if (waypoints.Length == 0) return;

        Vector3 lookAtGoal = new Vector3(waypoints[currWP].transform.position.x,
                                     this.transform.position.y,
                                     waypoints[currWP].transform.position.z);
                                     
        Vector3 direction = lookAtGoal - this.transform.position;

        this.transform.rotation = Quaternion.Slerp(this.transform.rotation,
                                                   Quaternion.LookRotation(direction),
                                                   Time.deltaTime * rotSpeed);

        if (direction.magnitude < accuracy)
        {
            currWP = (currWP + 1) % waypoints.Length;
        }

        this.transform.Translate(0, 0, speed * Time.deltaTime);
        // this.transform.position = Vector3.MoveTowards(this.transform.position, 
        // 	waypoints[currWP].transform.position,Time.deltaTime);
        
    }
}
