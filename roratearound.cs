using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class roratearound : MonoBehaviour
{
    public GameObject circle_point = null;
    GameObject[] planets;
    public GameObject p1=null;
    public GameObject p2=null;
    public bool flag = true;

    [System.Obsolete]
    void Start()
    {
        this.enabled = false;
        //planets = GameObject.FindGameObjectsWithTag("planet");
        //p1 = planets[0];
        //p2 = planets[1];

    }

    void Update()
    {

    }

    private void FixedUpdate()
    {   
        if (p1 && p2)
        {
            if (circle_point != null && flag)
            {
                p1.transform.RotateAround(circle_point.transform.position, Vector3.up, 0.5f);   //A绕着B的y轴进行旋转
            }
            if (circle_point != null && flag)
            {
                p2.transform.RotateAround(circle_point.transform.position, Vector3.up, 0.5f);   //A绕着B的y轴进行旋转
            }
        }

    }
}
