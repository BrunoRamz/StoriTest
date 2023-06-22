<h1><FONT SIZE=7>StoriTest</font></h1>

<p>
    <FONT SIZE=5>This module helps companies to send an <strong>Account Balance</strong> to their differents clients
    via e-mail.</font>
</p>
<img src=stori.jpeg alt="Stori Card Logo" width=150>

<br>

<h2>Pre-requisites:</h2>

<ul>
    <FONT SIZE=3>
    <li>Python3.8
        <a href="https://www.python.org/downloads/">Download python
        </a>
    </li>
    <li>Docker
        <a href="https://docs.docker.com/engine/install/ubuntu/">Download Docker
        </a>
    </li>
    </font>
</ul>

<br>

<h2>Quick Start:</h2>
<FONT SIZE=3>
<ol>
    <li>Create a virtual environment:
        <code>
        python3 -m venv [name_of_virtual_environment]
        </code>
    </li>
    <li>Install all the libraries:
        <code>
        pip install -r requirements.txt
        </code>
    </li>
    <li>Image creation:
        <code>
        docker build Dockerfile –t [tag_name]
        </code>
    </li>
    <li>Image execution:
        <code>
        docker run [image_name]
        </code>
    </li>
    </font>
</ol>

