using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

[System.Serializable]
public class LandmarkData
{
    public float x;
    public float y;
    public float z;
}

[System.Serializable]
public class PosePacket
{
    public LandmarkData nose;
    public LandmarkData right_wrist;
    public LandmarkData left_wrist;
    public LandmarkData right_knee;
    public LandmarkData left_knee;
    public LandmarkData right_elbow;
    public LandmarkData left_elbow;
    public LandmarkData right_ankle;
    public LandmarkData left_ankle;
    public LandmarkData right_shoulder;
    public LandmarkData left_shoulder;
    public LandmarkData right_hip;
    public LandmarkData left_hip;
}

public class NetworkManager : MonoBehaviour
{
    
    private UdpClient client;
    private Thread receiveThread;
    private string lastMessage = "";

    public int port = 5052;
    public PosePacket latestPose;

    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        client = new UdpClient(port);

        receiveThread = new Thread(ReceiveData);
        receiveThread.IsBackground = true;
        receiveThread.Start();

        Debug.Log("NetworkManager started on port " + port);
    }

    void ReceiveData()
    {
        IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, port);

        while (true)
        {
            byte[] data = client.Receive(ref anyIP);
            string text = Encoding.UTF8.GetString(data);

            try
            {
                latestPose = JsonUtility.FromJson<PosePacket>(text);
            }
            catch { }
        }
        
    }




    // Update is called once per frame
    void Update()
    {
        
    }
}