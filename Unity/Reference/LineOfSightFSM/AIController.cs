using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(AudioSource))]
public class AIController : MonoBehaviour 
{

    [SerializeField] private AudioClip[] m_ShootSounds;

    Animator anim;
    AudioSource m_AudioSource;
	public Transform player;

	// Use this for initialization
	void Start () {
		anim = this.GetComponent<Animator>();
        m_AudioSource = this.GetComponent<AudioSource>();
	}
	
	// Update is called once per frame
	void Update () 
	{
        //let all the state stuff be organised by the state machine in the animator
        //just update the animator transition conditions here and send them through
        anim.SetFloat("distance", Vector3.Distance(transform.position, player.transform.position));
        anim.SetFloat("visAngle", Vector3.Angle(this.transform.forward, player.transform.position - transform.position));
	}

    public void playShootingSound()
    {
        if (!m_AudioSource.isPlaying) {
            int n = Random.Range(1,m_ShootSounds.Length);

            m_AudioSource.clip = m_ShootSounds[n];
            m_AudioSource.PlayOneShot(m_AudioSource.clip);

            m_ShootSounds[n] = m_ShootSounds[0];
            m_ShootSounds[0] = m_AudioSource.clip;
        }
    }
}
