import 'package:flutter_bloc/flutter_bloc.dart';


abstract class CalculatorEvent {}

class NumberPressedEvent extends CalculatorEvent {
  final int number;
  NumberPressedEvent(this.number);
}

class ClearPressedEvent extends CalculatorEvent {}


class CalculatorState {
  final List<String> displayText;

  CalculatorState({required this.displayText});

  CalculatorState copyWith({List<String>? displayText}) {
    return CalculatorState(
      displayText: displayText ?? this.displayText,
    );
  }
}


class CalculatorBloc extends Bloc<CalculatorEvent, CalculatorState> {
  CalculatorBloc() : super(CalculatorState(displayText: [])) {
    on<NumberPressedEvent>((event, emit) {
      final newDisplayText = [...state.displayText, event.number.toString()];
      emit(state.copyWith(displayText: newDisplayText));
    });

    on<ClearPressedEvent>((event, emit) {
      final newDisplayText = [...state.displayText];
      if (newDisplayText.isNotEmpty) {
        newDisplayText.removeLast();
      }
      emit(state.copyWith(displayText: newDisplayText));
    });
  }
}