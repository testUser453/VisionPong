using UnityEngine;

public class Right_Elbow_Mover : MonoBehaviour
{
    public NetworkManager networkManager;
    public float scale = 5f;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (networkManager == null)
            return;

        if (networkManager.latestPose == null)
            return;
        
        if (networkManager.latestPose.right_elbow == null)
            return;

        // negated x and z coordinate to make the ball appear as mirror image
        Vector3 target = new Vector3(
            -networkManager.latestPose.right_elbow.x * scale,
            networkManager.latestPose.right_elbow.y * scale + 3.0f,
            -networkManager.latestPose.right_elbow.z * scale
        );

        /* automatically transform the Ball that this BallMover script is attached to based
            on the vector given to it in the "target"
            It is actually inherited by the parent classes of MonoBehavior 
        */
        transform.position = target;
    }
}
