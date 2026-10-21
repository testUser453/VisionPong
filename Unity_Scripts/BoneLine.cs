using UnityEngine;

public class BoneLine : MonoBehaviour
{
    public Transform jointA;
    public Transform jointB;

    private LineRenderer line;

    void Start()
    {
        line = gameObject.AddComponent<LineRenderer>();

        line.positionCount = 2;
        line.startWidth = 0.05f;
        line.endWidth = 0.05f;

        line.material = new Material(Shader.Find("Sprites/Default"));
    }

    void Update()
    {
        if (jointA == null || jointB == null) return;

        line.SetPosition(0, jointA.position);
        line.SetPosition(1, jointB.position);
    }
}