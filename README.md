# ReReelify
Replicate Instagram Theme Page Videos with Ease!

<p>Ever scrolled through Instagram and saw those amazing theme pages with others' videos on top of their logo and a small caption.</p>

<h2>Introduction</h2>

<p>ReReelify is your ultimate tool to help you create awesome Instagram Theme Pages with ease. With ReReelify you can use someone elses videos and put your logo and your preferred caption only keeping the original source video!</p>

<h2>Features</h2>
<ul>
    <li><strong>Automatic Cropping</strong>: Remove those pesky black bars from your videos seamlessly.</li>
    <li><strong>Logo Integration</strong>: Add your custom logo to videos.</li>
    <li><strong>Dynamic Text Generation</strong>: Use OCR and Open Source LLMs to create engaging text variations.</li>
    <li><strong>Aspect Ratio Conversion</strong>: Effortlessly convert videos to the 9:16 format ideal for social media.</li>
    <li><strong>Customizable Captions</strong>: Change how you want to keep the caption by editing the LLM prompt.</li>
</ul>

<h2>Note</h2>
<p>Here's what your source video should look like:</p>
<p float="left">
<img src="https://github.com/DilukshanN7/ReReelify/assets/65407969/0ef7edc6-2ed5-4740-8ff3-c7867ec12017" alt="Example Source Video" class="example-image" height="480" width="270">
</p>

<h2>Instructions</h2>
<ol>
    <li><strong>Install Tesseract-OCR</li>
    <pre><code>https://github.com/UB-Mannheim/tesseract/wiki</code></pre>
    <li><strong>Clone the Repository</strong>: Clone this repository to your local machine.</li>
    <pre><code>git clone https://github.com/yourusername/ReReelify.git</code></pre>
    <li><strong>Install Dependencies</strong>: Install the required Python packages.</li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li><strong>Configure Parameters</strong>: Adjust the parameters at the bottom of the script to customize your video processing.</li>
    <li><strong>Hugging Face Account</strong>: Provide your Hugging Face account credentials in the 9th line.</li>
    <li><strong>Run the Script</strong>: Execute the script to start processing your videos.</li>
    <pre><code>python ReReelify.py</code></pre>

<h2>Parameters</h2>
<ul>
    <li><strong>input_folder</strong>: Path to your input video folder.</li>
    <li><strong>output_folder</strong>: Path to your output video folder.</li>
    <li><strong>logo_path</strong>: Path to your custom logo image.</li>
    <li><strong>logo_scale</strong>: Scale of the logo relative to the video width (e.g., 0.2 for 20%).</li>
    <li><strong>text_padding</strong>: Padding for the text from the video edges.</li>
    <li><strong>element_padding</strong>: Padding between logo, text, and video.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
