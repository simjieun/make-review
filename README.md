
# 리뷰 제조기 🤖

## Project Description
리뷰 제조기는 사용자가 입력한 업종과 별점을 바탕으로 리뷰를 생성해주는 웹 애플리케이션입니다. 리뷰는 사실에 기반하거나 감성적인 형태로 생성될 수 있으며, 이모지도 포함됩니다. 이 애플리케이션은 Streamlit을 사용하여 개발되었습니다.

## Features
- 사용자가 입력한 업종과 별점에 기반한 리뷰 생성
- 감성적인 리뷰 작성 옵션

## Installation and Setup
1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd review-generator
   ```

2. **Set up the virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the OpenAI API**:
   - Create an account on OpenAI and get your API key.
   - Create a `.env` file in the root directory and add your API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage
1. **Enter the industry**: Input the industry you want a review for.
2. **Select the star rating**: Choose the star rating (1 to 5 stars).
3. **Generate review**: Click the "리뷰 생성" button to generate the review.

The generated review will include a description based on the provided industry and star rating, with optional emotional content and emojis.

## Dependencies
- Python 3.8+
- Streamlit
- OpenAI API
- Python libraries specified in `requirements.txt`

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
