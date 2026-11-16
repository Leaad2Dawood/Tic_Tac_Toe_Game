import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", page_icon="⭕", layout="centered")

st.title("⭕ Tic-Tac-Toe")
st.caption("A two-player game built with Streamlit and NumPy.")


def new_game():
    st.session_state.board = [[0 for _ in range(3)] for _ in range(3)]
    st.session_state.current = 1
    st.session_state.winner = None
    st.session_state.draw = False


def get_result(board):
    lines = board + [[board[r][c] for r in range(3)] for c in range(3)]
    lines += [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)],
    ]
    for line in lines:
        if sum(line) == 3:
            return 1
        if sum(line) == -3:
            return -1
    if all(cell != 0 for row in board for cell in row):
        return 0
    return None


if "board" not in st.session_state:
    new_game()

board = st.session_state.board
winner = st.session_state.winner

if winner == 1:
    st.success("🎉 X wins!")
elif winner == -1:
    st.success("🎉 O wins!")
elif st.session_state.draw:
    st.info("It’s a draw!")
else:
    player = "X" if st.session_state.current == 1 else "O"
    st.subheader(f"{player}’s turn")

# Three columns per row keep the board compact and centered.
for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        mark = {0: "·", 1: "❌", -1: "⭕"}[board[r][c]]
        with cols[c]:
            if st.button(
                mark,
                key=f"cell-{r}-{c}",
                use_container_width=True,
                disabled=winner is not None or st.session_state.draw or board[r][c] != 0,
            ):
                board[r][c] = st.session_state.current
                result = get_result(board)
                if result == 0:
                    st.session_state.draw = True
                elif result in (1, -1):
                    st.session_state.winner = result
                else:
                    st.session_state.current *= -1
                st.rerun()

st.button("🔄 New game", on_click=new_game, use_container_width=True)
