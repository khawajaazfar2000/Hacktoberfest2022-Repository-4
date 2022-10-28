#include <iostream>
using namespace std;

struct AVL
{
    int id;
    AVL *left = NULL, *right = NULL;
};
AVL *root = NULL;

AVL *right_right_Rotation(AVL *parent)
{
    AVL *curr = new AVL;
    curr = parent->right;
    parent->right = curr->left;
    curr->left = parent;
    return curr;
}
AVL *right_left_Rotation(AVL *parent)
{
    AVL *curr = new AVL;
    curr = parent->right->left;
    parent->right->left = curr->right;
    curr->right = parent->right;
    parent->right = curr->left;
    curr->left = parent;
    return curr;
}
AVL *left_left_Rotation(AVL *parent)
{
    AVL *curr = new AVL;
    curr = parent->left;
    parent->left = curr->right;
    curr->right = parent;
    return curr;
}
AVL *left_right_Rotation(AVL *parent)
{
    AVL *curr = new AVL;
    curr = parent->left->right;
    parent->left->right = curr->left;
    curr->left = parent->left;
    parent->left = curr->right;
    curr->right = parent;
    return curr;
}
int max(int leftHeight, int rightHeight)
{
    if (leftHeight > rightHeight)
    {
        return leftHeight;
    }
    return rightHeight;
}
int findHeight(AVL *p)
{
    if (p == NULL)
    {
        return 0;
    }
    int leftHeight = findHeight(p->left);
    int righttHeight = findHeight(p->right);
    return max(leftHeight, righttHeight) + 1;
}
int balance_Factor(AVL *p)
{
    int balanceFactor = 0;
    if (p != NULL)
    {
        int heightofLeft = findHeight(p->left);
        int heightofright = findHeight(p->right);
        balanceFactor = heightofLeft - heightofright;
    }
    return balanceFactor;
}
void inorder_Traversal(AVL *p)
{
    if (p != NULL)
    {
        inorder_Traversal(p->left);
        cout << "ID: " << p->id << endl;
        inorder_Traversal(p->right);
    }
}
void deleteNode(int id)
{
}

void insert(int id)
{
    AVL *curr = new AVL;
    curr->id = id;
    if (root == NULL)
    {
        root = curr;
    }
    else
    {
        AVL *p = new AVL, *prev = new AVL;
        p = root;
        prev = NULL;
        prev = p;
        if (p->id < curr->id)
        {
            p = p->right;
        }
        else
        {
            p = p->left;
        }

        if (prev->id < curr->id)
        {
            prev->right = curr;
        }
        else
        {
            prev->left = curr;
        }
    }
}
void autoInsert()
{
    int arr[] = {80, 100, 110, 60, 95, 60, 50, 65, 75};

    for (int i = 0; i < 9; i++)
    {
        insert(arr[i]);
    }
}

void opt()
{
    cout << "\n1-Auto Insert Node in AVL Tree" << endl
         << "2- Check Height of the Binary Search Tree" << endl
         << "3- Remove a node from Binary Search Tree" << endl
         << "4- Find Balance Factor of Tree" << endl
         << "5- Inorder Traversal of Binary Search Tree" << endl
         << "0- Terminate a program" << endl;

    cout << "\nEnter your Choice: ";
    int choice;
    cin >> choice;

    switch (choice)
    {
    case 1:
        cout << "\nAUTO INSERT NODE IN AVL TREE METHOD" << endl;
        autoInsert();
        opt();
        break;

    case 2:
        cout << "\nCHECK HEIGHT OF AVL TREE METHOD" << endl;
        cout << "Height of AVL Tree is: " << findHeight(root) << endl;
        opt();
        break;

    case 3:
        cout << "\nREMOVE A NODE FROM AVL TREE METHOD" << endl;
        opt();
        break;

    case 4:
        cout << "\nBALANCE FACTOR FINDER OF AVL TREE METHOD" << endl;
        cout << "Balance factor of AVL TREE is: " << balance_Factor(root) << endl;
        opt();
        break;

    case 5:
        cout << "\nIORDER TRAVERSAL of AVL TREE METHOD" << endl;
        inorder_Traversal(root);
        opt();
        break;

    case 0:
        cout << "\nProcess Terminated Successfully" << endl;
        break;

    default:
        cout << "Invalid Choice Try Again!!" << endl;
        opt();
        break;
    }
}
int main()
{
    opt();
    return 0;
}
