using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(AudioSource))]
public class AIController : MonoBehaviour {

    [SerializeField] private AudioClip[] m_ShootSounds;

    Animator anim;
    AudioSource m_AudioSource;
	public Transform player;
	
    float m_StepCycle;
    float m_NextStep;
	float rotationSpeed = 2.0f;
    [Range(0.0f, 10.0f)]
	public float speed = 4.0f;
    [Range(0.0f, 30.0f)]
	public float visDist = 20.0f;
    [Range(0.0f, 150.0f)]
	public float visAngle = 60.0f;
    [Range(0.0f, 15.0f)]
	public float shootDist = 8.0f;

	string state = "IDLE";

	// Use this for initialization
	void Start () {
		anim = this.GetComponent<Animator>();
        m_AudioSource = this.GetComponent<AudioSource>();

        m_NextStep = m_StepCycle / 2f;
	}
	
	// Update is called once per frame
	void Update () 
	{
		Vector3 direction = player.position - this.transform.position;
		float angle = Vector3.Angle(direction, this.transform.forward);
		
		if(direction.magnitude < visDist && angle < visAngle)
		{
			
			direction.y = 0;

			this.transform.rotation = Quaternion.Slerp(this.transform.rotation,
										Quaternion.LookRotation(direction), 
										Time.deltaTime * rotationSpeed);
              
			if(direction.magnitude > shootDist)
			{ 
				if(state != "RUNNING")
				{ 
					state = "RUNNING";	
					anim.SetTrigger("isRunning");
				}	
			}
			else
			{
				if(state != "SHOOTING")
				{ 
					state = "SHOOTING";
					anim.SetTrigger("isShooting");
				}
                playShootingSound();
			}

		}
		else
		{
			if(state != "IDLE")
			{ 
				state = "IDLE";
				anim.SetTrigger("isIdle");
			}
		}

		if(state == "RUNNING")
			this.transform.Translate(0,0, Time.deltaTime * speed);

	}

    private void playShootingSound()
    {
        if (!m_AudioSource.isPlaying) {
            int n = Random.Range(1,m_ShootSounds.Length);

            m_AudioSource.clip = m_ShootSounds[n];
            m_AudioSource.PlayOneShot(m_AudioSource.clip);

            m_ShootSounds[n] = m_ShootSounds[0];
            m_ShootSounds[0] = m_AudioSource.clip;

            //m_NextStep = m_StepCycle + 1f;
        }
    }
}
