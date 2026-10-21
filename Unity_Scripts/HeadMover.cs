using UnityEngine;

public class HeadMover : MonoBehaviour
{
    public NetworkManager networkManager;
    public float scale = 5f;

    void Update()
    {
        if (networkManager == null)
            return;

        if (networkManager.latestPose == null)
            return;
        
        if (networkManager.latestPose.nose == null)
            return;

        // commented x and z coordinate to make the ball appear as mirror image
        Vector3 target = new Vector3(
            -networkManager.latestPose.nose.x * scale,
            networkManager.latestPose.nose.y * scale + 3.0f,
            -networkManager.latestPose.nose.z * scale
        );

        /* automatically transform the Ball that this BallMover script is attached to based
            on the vector given to it in the "target"
            It is actually inherited by the parent classes of MonoBehavior 
        */
        transform.position = target;
    }
}
