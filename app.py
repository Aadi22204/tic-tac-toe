import streamlit as st
import numpy as np

from game_logic import create_board, check_winner


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Tic-Tac-Toe",
    page_icon="🎮",
    layout="centered"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .player-card {
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
    }

    .winner-box {
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
    }

    .board-cell {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "board" not in st.session_state:
    st.session_state.board = create_board()

if "current_player" not in st.session_state:
    st.session_state.current_player = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "winner" not in st.session_state:
    st.session_state.winner = None

if "x_score" not in st.session_state:
    st.session_state.x_score = 0

if "o_score" not in st.session_state:
    st.session_state.o_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def reset_game():
    """Reset the current game."""
    st.session_state.board = create_board()
    st.session_state.current_player = 1
    st.session_state.game_over = False
    st.session_state.winner = None


def reset_scores():
    """Reset game and scoreboard."""
    reset_game()
    st.session_state.x_score = 0
    st.session_state.o_score = 0
    st.session_state.draw_score = 0


def make_move(row, col):
    """Make a move on the selected cell."""

    if st.session_state.game_over:
        return

    board = st.session_state.board

    # Cell already occupied
    if board[row, col] != 0:
        st.warning("⚠️ This cell is already occupied!")
        return

    # Place player's mark
    board[row, col] = st.session_state.current_player

    # Check result
    result = check_winner(board)

    if result is not None:

        st.session_state.game_over = True
        st.session_state.winner = result

        if result == "X":
            st.session_state.x_score += 1

        elif result == "O":
            st.session_state.o_score += 1

        elif result == "DRAW":
            st.session_state.draw_score += 1

    else:
        # Switch player
        st.session_state.current_player *= -1


def get_symbol(value):
    """Convert board value into display symbol."""

    if value == 1:
        return "❌"

    if value == -1:
        return "⭕"

    return " "


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎮 Tic-Tac-Toe</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A Python + NumPy + Streamlit Game</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SCOREBOARD
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("❌ Player X", st.session_state.x_score)

with col2:
    st.metric("⭕ Player O", st.session_state.o_score)

with col3:
    st.metric("🤝 Draws", st.session_state.draw_score)


st.divider()


# --------------------------------------------------
# CURRENT PLAYER
# --------------------------------------------------

if not st.session_state.game_over:

    if st.session_state.current_player == 1:
        st.info("🎯 **Player X's Turn**")
    else:
        st.info("🎯 **Player O's Turn**")


# --------------------------------------------------
# GAME RESULT
# --------------------------------------------------

if st.session_state.game_over:

    if st.session_state.winner == "X":

        st.success("🎉 Player X Wins!")

    elif st.session_state.winner == "O":

        st.success("🎉 Player O Wins!")

    else:

        st.warning("🤝 It's a Draw!")


# --------------------------------------------------
# GAME BOARD
# --------------------------------------------------

board = st.session_state.board

for row in range(3):

    cols = st.columns(3)

    for col in range(3):

        with cols[col]:

            value = board[row, col]
            symbol = get_symbol(value)

            if value == 0:

                st.button(
                    "⬜",
                    key=f"cell_{row}_{col}",
                    use_container_width=True,
                    on_click=make_move,
                    args=(row, col)
                )

            else:

                st.button(
                    symbol,
                    key=f"cell_{row}_{col}",
                    use_container_width=True,
                    disabled=True
                )


# --------------------------------------------------
# CONTROLS
# --------------------------------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.button(
        "🔄 New Game",
        use_container_width=True,
        on_click=reset_game
    )

with col2:

    st.button(
        "🗑️ Reset Score",
        use_container_width=True,
        on_click=reset_scores
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🎮 Game Information")

    st.write(
        """
        **How to play**

        1. Player X starts the game.
        2. Select an empty cell.
        3. Player O plays next.
        4. Get three symbols in a row.
        5. First player to complete a row,
           column, or diagonal wins.
        """
    )

    st.divider()

    st.subheader("🛠️ Technologies")

    st.write("🐍 Python")
    st.write("🔢 NumPy")
    st.write("🎨 Streamlit")

    st.divider()

    st.caption(
        "Built as a Python portfolio project."
    )